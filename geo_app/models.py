from django.db import models

from osm_field.fields import LatitudeField, LongitudeField, OSMField
from django_admin_geomap import GeoItem
from django.contrib.auth.models import User


class MyModel(models.Model, GeoItem):
    location = OSMField(lat_field='latitude', lon_field='longitude', verbose_name='Локация')
    latitude = LatitudeField(verbose_name='Географическая широта')
    longitude = LongitudeField(verbose_name='Географическая долгота')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    @property
    def geomap_longitude(self):
        return '' if self.longitude is None else str(self.longitude)

    @property
    def geomap_latitude(self):
        return '' if self.latitude is None else str(self.latitude)

    @property
    def geomap_icon(self):
        return self.default_icon

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'Локации'
        verbose_name = 'Локация'
        ordering = ['location']
