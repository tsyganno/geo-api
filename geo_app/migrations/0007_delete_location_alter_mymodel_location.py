# Generated by Django 4.1.2 on 2022-10-22 10:17

from django.db import migrations
import osm_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0006_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='location',
            field=osm_field.fields.OSMField(lat_field='latitude', lon_field='longitude', verbose_name='Локация'),
        ),
    ]
