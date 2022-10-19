from django.db import models


class City(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    federal_district = models.CharField(max_length=50, verbose_name='Федеральный округ')
    region = models.CharField(max_length=50, verbose_name='Область')
    city = models.CharField(max_length=20, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house = models.CharField(max_length=50, verbose_name='Номер дома')
    block = models.CharField(max_length=50, verbose_name='Блок дома')
    flat = models.CharField(max_length=50, verbose_name='Номер квартиры')
    geo_lat = models.FloatField(verbose_name='Географическая широта')
    geo_lon = models.FloatField(verbose_name='Географическая долгота')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'
        ordering = ['city']
