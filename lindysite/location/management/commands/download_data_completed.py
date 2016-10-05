from django.core.management.base import BaseCommand, CommandError
import os
from django.db import IntegrityError
from . import files,baseurl
from location.utils import download

class Command(BaseCommand):
    help = ''
    app_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/../..')
    data_dir = os.path.join(app_dir, 'data')

    def add_arguments(self, parser):
        parser.add_argument('--download', action='store_true',default=False,help='./manage.py dump_cities --download')

    def handle(self, *args, **options):
        if options['download']:
            for myfile in files:
                print(files[myfile]['filename'])
                result = download(baseurl+files[myfile]['filename'], self.data_dir,files[myfile]['filename'])
                if not result:
                   download(baseurl+files[myfile]['zipfilename'], self.data_dir,files[myfile]['zipfilename'])
