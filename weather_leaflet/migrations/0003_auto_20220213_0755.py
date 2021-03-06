# Generated by Django 4.0.2 on 2022-02-13 07:30

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path


DATA_FILENAME = 'locations.json'
def load_data(apps, schema_editor):
    Location = apps.get_model('weather_leaflet','Location')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({latitude} {longitude})', srid=4326)
                    Location(name=name, location = location).save()
            except KeyError:
                pass 
class Migration(migrations.Migration):

    dependencies = [
        ('weather_leaflet', '0002_rename_locations_location'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
