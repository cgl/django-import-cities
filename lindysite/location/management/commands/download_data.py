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
        pass

    def handle(self, *args, **options):
        if options['download']:
            pass
