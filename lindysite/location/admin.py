from django.contrib import admin
from location.models import City, Country

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name','timezone']

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
