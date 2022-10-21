# Generated by Django 4.1.2 on 2022-10-21 14:09

from django.db import migrations, models
import osm_field.fields
import osm_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0003_alter_city_block_alter_city_city_alter_city_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', osm_field.fields.OSMField(lat_field='latitude', lon_field='longitude')),
                ('latitude', osm_field.fields.LatitudeField(validators=[osm_field.validators.validate_latitude])),
                ('longitude', osm_field.fields.LongitudeField(validators=[osm_field.validators.validate_longitude])),
            ],
        ),
    ]
