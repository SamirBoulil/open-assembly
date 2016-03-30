# coding: utf-8

import os
import json
import time
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from slugify import slugify
from open_assembly.models import Deputy
from open_assembly.models import Mandate
from open_assembly.models import Circonscription


def import_deputies(filepath):
    """ Loads a list of deputies
    """
    with open(filepath, 'r') as deputy_file:
        print("loaded file")
        deputy_list = json.load(deputy_file)
        i = 0
        for deputy in deputy_list['export']['acteurs']['acteur']:
            import_deputy(deputy)
            i = i+1

        print("%d deputies were loaded" % i)


def import_deputy(deputy_info):
    """
    Loads information about deputies in the database like, personal information,
    circoscription where they were elected as well as their mandates.

    :param deputy_info: deputy information
    :type deputy_info: dict
    """
    mandate_info = get_assembly_mandate(deputy_info)
    if mandate_info is not False:
        deputy = get_or_create_deputy(deputy_info)
        circonscription = get_or_create_circonscription(mandate_info)
        mandate = get_or_create_mandate(mandate_info, deputy, circonscription)


def get_assembly_mandate(deputy_info):
    """ returns wether the deputy has a assembly mandate

    :param deputy_info: deputy information
    :type deputy_info: dict
    :returns: true if is an assembly deputy
    :rtype: boolean|mandate dict object
    """
    for mandate in deputy_info['mandats']['mandat']:
        if mandate.get('typeOrgane', '') == "ASSEMBLEE":
            return mandate
    return False

def get_deputy_email(deputy_info):
    """ Returns the email of a deputy if available

    :param deputy_info: deputy information
    :type deputy_info: dict
    :returns: email address or None
    """
    if isinstance(deputy_info['adresses']['adresse'], dict):
        address = deputy_info['adresses']['adresse']
        if address['@xsi:type'] == 'AdresseMail_Type' and address['valElec'] != '':
            return address['valElec']
    else:
        for address in deputy_info['adresses']['adresse']:
            if address['@xsi:type'] == 'AdresseMail_Type' and address['valElec'] != '':
                return address['valElec']
    return None


def get_or_create_deputy(deputy_info):
    """ Creates or retrieves information about a deputy

    :param deputy_info: information about a deputy
    :type deputy_info: dict
    :returns: model representing a deputy
    """
    try:
        return Deputy.objects.get(id=deputy_info['uid']['#text'])

    except ObjectDoesNotExist:
        deputy = Deputy()
        deputy.id = deputy_info['uid']['#text']
        deputy.name = deputy_info['etatCivil']['ident']['nom']
        deputy.surname = deputy_info['etatCivil']['ident']['prenom']
        deputy.slug = slugify(deputy.name + '_' + deputy.surname)
        deputy.sex = deputy_info['etatCivil']['ident']['civ'] == 'Mme' # 1 = Women
        deputy.mail = get_deputy_email(deputy_info)
        deputy.birth_date = datetime.strptime(deputy_info['etatCivil']['infoNaissance']['dateNais'], '%Y-%m-%d')
        deputy.birth_town = deputy_info['etatCivil']['infoNaissance']['villeNais']
        deputy.birth_department = deputy_info['etatCivil']['infoNaissance']['depNais']
        deputy.birth_country = deputy_info['etatCivil']['infoNaissance']['paysNais']
        deputy.work_name = deputy_info['profession']['libelleCourant']
        deputy.work_category = deputy_info['profession']['socProcINSEE']['catSocPro']
        deputy.work_familly = deputy_info['profession']['socProcINSEE']['famSocPro']
        deputy.save()

        return deputy


def get_or_create_circonscription(mandate_info):
    """ Creates or retrieves information about a circonscription

    :param mandate_info: information about a mandate
    :type mandate_info: dict
    :returns: model representing a circonscription
    """
    try:
        return Circonscription.objects.get(
            num_circo=mandate_info['election']['lieu']['numCirco'],
            num_department=mandate_info['election']['lieu']['numDepartement'])

    except ObjectDoesNotExist:
        circonscription = Circonscription()
        circonscription.department = mandate_info['election']['lieu']['departement']
        circonscription.num_circo  = mandate_info['election']['lieu']['numCirco']
        circonscription.num_department = mandate_info['election']['lieu']['numDepartement']
        circonscription.region = '' if mandate_info['election']['lieu']['region'] is None else mandate_info['election']['lieu']['region']
        circonscription.save()
        return circonscription


def get_or_create_mandate(mandate_info, deputy, circonscription):
    """ Creates or retrieves information about a mandate

    :param mandate_info: information about a mandate
    :type mandate_info: dict
    :returns: model representing a  mandate
    """
    try:
        return Mandate.objects.get(id=mandate_info['uid'])

    except ObjectDoesNotExist:
        mandate = Mandate()
        mandate.id = mandate_info['uid']
        mandate.start_date = datetime.strptime(mandate_info['mandature']['datePriseFonction'], '%Y-%m-%d')
        mandate.seat_number = '' if mandate_info['mandature']['placeHemicycle'] is None else mandate_info['mandature']['placeHemicycle']
        mandate.election_cause_mandat = mandate_info['election']['causeMandat']
        mandate.legislature = mandate_info['legislature']
        mandate.circonscription_id = circonscription.id

        if 'suppleants' in mandate_info.keys() \
                and mandate_info['suppleants'] is not None:
                substitute, _created = Deputy.objects.get_or_create(id=mandate_info['suppleants']['suppleant']['suppleantRef'])
                substitute.save()
                deputy.substitutes.add(substitute)
                deputy.save()

        mandate.save()
        mandate.deputies.add(deputy)
        mandate.save()

        return  mandate

