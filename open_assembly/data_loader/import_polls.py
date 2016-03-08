# coding: utf-8

import os 
import json
import time
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from slugify import slugify

from open_assembly.models import Deputy
from open_assembly.models import Mandate
from open_assembly.models import Circonscription
from open_assembly.models import Poll
from open_assembly.models import Vote
from open_assembly.models import Group


def import_polls(filepath):
    """ Main loop to iterate over polls and load them into database.
    """
    with open(filepath, 'r') as poll_file:
        print("loaded file")
        poll_list = json.load(poll_file)
        for i, poll in enumerate(poll_list['scrutins']['scrutin']):
            with transaction.atomic():
                import_poll(poll)
                if i%10 == 0:
                    print("poll %d" % i)

        print("%d polls were loaded" % i)


def import_poll(poll_info):
    """ Import poll_info information as well as votes
    """
    poll = get_or_instanciate_poll(poll_info)
    poll.save()

    votes = []
    i=0
    for group_info in poll_info['ventilationVotes']['organe']['groupes']['groupe']:
        group, _created = Group.objects.get_or_create(id=group_info['organeRef'])
        group.save()
        i = i+1

        # not voting people
        try:
            create_or_update_votes(group_info['vote']['decompteNominatif']['nonVotants']['votant'], 3, group, poll)
        except Exception as e:
            pass
            # print("No NOT VOTING votes")
            
        try:
            create_or_update_votes(group_info['vote']['decompteNominatif']['pours']['votant'], 1, group, poll)
        except Exception as e:
            pass
            # print("No YES votes")

        try:
            create_or_update_votes(group_info['vote']['decompteNominatif']['contres']['votant'], 0, group, poll)
        except Exception as e:
            pass
            # print("No NO votes")

        try:
            create_or_update_votes(group_info['vote']['decompteNominatif']['abstentions']['votant'], 2, group, poll)
        except Exception as e:
            pass
            # print("No abstention votes")


def create_or_update_votes(votes, vote_value, group, poll):
    """
    """
    if isinstance(votes, list):
        for vote_info in votes:
            get_or_update_vote(vote_info, vote_value, group, poll)
    else:
        get_or_update_vote(votes, vote_value, group, poll)


def get_or_update_vote(vote_info, vote_value, group, poll):
    try:
        deputy = Deputy.objects.get(id=vote_info['acteurRef'])
        if deputy.group is None:
            deputy.group = group
            deputy.save()
        mandate, _created = Mandate.objects.get_or_create(
                id=vote_info['mandatRef']
        )
        mandate.save()

        vote, _created = Vote.objects.get_or_create(
                mandate=mandate,
                decision=vote_value,
                poll=poll)
        vote.save()
    except ObjectDoesNotExist as e:
        pass
        # print(e)
        # print("Unkown deputy ref: %s" % vote_info['acteurRef'])
    except Exception as e:
        pass
        # print(e)
        # import pdb; pdb.set_trace()
        # print(e)

         
def get_or_instanciate_poll(poll_info):
    """
    """
    try:
        return Poll.objects.get(id=poll_info['uid'])
    except ObjectDoesNotExist:
        poll = Poll()
        poll.id = poll_info['uid']
        poll.title = poll_info['titre']
        poll.legislature = poll_info['legislature']
        poll.session_ref = poll_info['sessionRef']
        poll.seanceRef = poll_info['seanceRef']
        poll.asked_by = poll_info['demandeur']['texte']
        poll.poll_date = datetime.strptime(poll_info['dateScrutin'], '%Y-%m-%d')
        poll.number_people_voting = int(poll_info['syntheseVote']['nombreVotants'])
        poll.number_votes_made = int(poll_info['syntheseVote']['suffragesExprimes'])
        poll.number_votes_required = int(poll_info['syntheseVote']['nbrSuffragesRequis'])
        poll.number_votes_no = int(poll_info['syntheseVote']['decompte']['nonVotant'])
        poll.number_votes_yes = int(poll_info['syntheseVote']['decompte']['pour'])
        poll.number_votes_dk = int(poll_info['syntheseVote']['decompte']['contre'])
        poll.number_votes_not_voting = int(poll_info['syntheseVote']['decompte']['abstention'])
        poll.is_accepted = True if poll.number_votes_yes >= poll.number_votes_required else False
        poll.is_solemn = True if poll_info['typeVote']['libelleTypeVote'] == 'scrutin public solennel' else False

        return poll
