from django.db import models

from osm_field.fields import LatitudeField, LongitudeField, OSMField


class MyModel(models.Model):
    location = OSMField(lat_field='latitude', lon_field='longitude')
    latitude = LatitudeField()
    longitude = LongitudeField()


class City(models.Model):
    country = models.CharField(null=True, max_length=50, verbose_name='Страна')
    federal_district = models.CharField(null=True, max_length=50, verbose_name='Федеральный округ')
    region = models.CharField(null=True, max_length=50, verbose_name='Область')
    city = models.CharField(null=True, max_length=20, verbose_name='Город')
    street = models.CharField(null=True, max_length=50, verbose_name='Улица')
    house = models.CharField(null=True, max_length=50, verbose_name='Номер дома')
    block = models.CharField(null=True, max_length=50, verbose_name='Блок дома')
    flat = models.CharField(null=True, max_length=50, verbose_name='Номер квартиры')
    geo_lat = models.CharField(null=True, max_length=50, verbose_name='Географическая широта')
    geo_lon = models.CharField(null=True, max_length=50, verbose_name='Географическая долгота')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'
        ordering = ['city']
