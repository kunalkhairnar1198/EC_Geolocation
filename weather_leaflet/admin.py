from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location

# Register your models here.

@admin.register(Location)
class Weather(OSMGeoAdmin):
    list_display = ('name', 'location')

