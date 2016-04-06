from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(editable=False, default=False, verbose_name='Deleted')
    class Meta:
        abstract = True

class Country(BaseModel):
    name = models.CharField(max_length=64, verbose_name = u'Country name',unique=True)
    slug = models.SlugField()
    geonameid = models.IntegerField(null=True)
    continent = models.CharField(max_length=2)
    code = models.CharField(max_length=2, db_index=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "countries"
        verbose_name = "country"
        ordering = ['name']


class City(BaseModel):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=64, verbose_name = u'City name',unique=True)
    slug = models.SlugField()
    timezone = models.CharField(max_length=40)
    name_std = models.CharField(max_length=200, db_index=True, verbose_name="standard name")

    population = models.IntegerField(null=True)
    elevation = models.IntegerField(null=True)
    kind = models.CharField(max_length=11,null=True)  # http://www.geonames.org/export/codes.html
    image = models.ImageField(null=True, blank=True, verbose_name="city_image")
    geonameid = models.IntegerField(null=True)
    order_number = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
        verbose_name = "City"
        ordering = ['order_number','name']

    def fullname(self):
        return "%s, %s" % (self.name, self.country.name)

    follows = models.ManyToManyField(User,through="FollowsCity", related_name="follow_city")


class FollowsCity(models.Model):
    user = models.ForeignKey(User)
    city = models.ForeignKey(City)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "city"),)
