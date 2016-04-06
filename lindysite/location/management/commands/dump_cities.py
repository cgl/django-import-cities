from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from ...models import City,Country
import os,logging
from tqdm import tqdm
from django.db import IntegrityError
from . import files,city_types


class Command(BaseCommand):
    help = 'Import City data from geonames.org'
    app_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/../..')
    data_dir = os.path.join(app_dir, 'data')
    logger = logging.getLogger("cities")

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--countries', action='store_true',default=False,help='./manage.py fetch_cities --countries')
        parser.add_argument('--cities', action='store_true',default=False,help='./manage.py fetch_cities --cities')

    def handle(self, *args, **options):
        if options['countries']:
            filename = files['country']['filename']
            fields = files['country']['fields']
            self.logger.info("Importing country data")
            file_obj = open(os.path.join(self.data_dir, filename), 'r', encoding='utf-8')
            data = self.get_data(file_obj,fields)
            self.import_country(data)
        if options['cities']:
            filename = files['city']['filename']
            fields = files['city']['fields']
            self.logger.info("Importing city data")
            file_obj = open(os.path.join(self.data_dir, filename), 'r', encoding='utf-8')
            data = self.get_data(file_obj,fields)
            self.import_city(data)

    def add_city_from_line(self,item,force=False):
        if not force and item['featureCode'] not in city_types:
            return
        if not force and int(item['population'])<500000:
            return
        country_code = item['countryCode']
        try:
            country = self.country_index[country_code]
        except:
            self.logger.warning("City: '%s' -> Cannot find country: %s -- skipping",
                                item['name'], country_code)
            return
        try:
                city, created = City.objects.update_or_create(name = item['name'],
                                              name_std = item['asciiName'],
                                              country = country,
                                              slug = slugify(item['asciiName']),
                                              timezone = item['timezone'])

                city.kind = item['featureCode']
                city.population = int(item['population'])
                try:
                    city.elevation = int(item['elevation'])
                except:
                    pass
                city.save()
        except IntegrityError:
                print("*********** %s *************" %item['name'])
                return
        try:
                city.geonameid = int(item['geonameid'])
                city.save()
        except:
                return
        self.logger.info("Added city: %s", city)
        #print("Added city: %s" %city)

    def import_city(self,data):
        total = 47385 #sum(1 for _ in data)
        self.build_country_index()
        self.logger.info("Importing city data")
        for item in tqdm(data,total=total, desc="Importing cities"):
            self.add_city_from_line(item)


    def build_country_index(self):
        if hasattr(self, 'country_index'):
            return
        self.logger.info("Building country index")
        self.country_index = {}
        for obj in tqdm(Country.objects.all(),
                        total=Country.objects.count(),
                        desc="Building country index"):
            self.country_index[obj.code] = obj

    def import_country(self,data):
        for item in tqdm([d for d in data if int(d['population']) > 2000000 ],
                         desc="Importing countries..."):
            self.logger.info(item)
            country = Country()
            try:
                country.geonameid = int(item['geonameid'])
            except:
                continue

            country.name = item['name']
            country.slug = slugify(country.name)
            country.code = item['code']
            country.continent = item['continent']
            country.save()

    def get_data(self,file_obj,fields):
        for row in file_obj:
            if not row.startswith('#'):
                yield dict(list(zip(fields, row.split("\t"))))
