# coding: utf-8


from django.core.management.base import BaseCommand, CommandError

from data_loader.import_deputies import import_deputies

from data_loader.settings import DEPUTY_DATA_URL


class Command(BaseCommand):
    help = 'Imports decrees, deputy information and votes'

    def add_arguments(self, parser):
        parser.add_argument('--overwrite',
                '-o',
                dest='overwrite',
                default=False,
                help="If TRUE truncate the current database before "
                "importing data")

        parser.add_argument('--path',
                dest='path',
                default='/var/tmp/AMO10_deputes_actifs_mandats_actifs_organes_XIV.json',
                type=str,
                help="file path to the deputy file information")

    def handle(self, *args, **options):
        overwrite = options.get('overwrite')
        filepath = options.get('path')
        filepath = '/Users/Akeneo/Downloads/AMO10_deputes_actifs_mandats_actifs_organes_XIV.json'
        print("filepath %s" % filepath)

        if overwrite:
            raise NotImplemented("Dump all data from db feature")
            return
        
        import_deputies(filepath)

        


