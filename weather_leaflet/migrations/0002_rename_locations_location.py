# Generated by Django 4.0.2 on 2022-02-12 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_leaflet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]
