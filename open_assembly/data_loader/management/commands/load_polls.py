# coding: utf-8


from django.core.management.base import BaseCommand, CommandError

from data_loader.import_polls import import_polls

from data_loader.settings import DEPUTY_DATA_URL


class Command(BaseCommand):
    help = 'Import polls and votes'

    def add_arguments(self, parser):
        parser.add_argument('--overwrite',
                '-o',
                dest='overwrite',
                default=False,
                help="If TRUE truncate the current database before "
                "importing data")

        parser.add_argument('--path',
                dest='path',
                default='/var/tmp/Scrutins_XV.json',
                type=str,
                help="file path to the deputy file information")

    def handle(self, *args, **options):
        overwrite = options.get('overwrite')
        filepath = options.get('path')

        if overwrite:
            raise NotImplemented("Dump all data from db feature")
            return
        
        import_polls(filepath)

