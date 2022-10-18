from django.db import models


# class City(models.Model):
#     address = models.CharField(max_length=50, verbose_name='Адрес')
#     postal_code = models.IntegerField(max_length=10, verbose_name='Почтовый Код')
#     country = models.CharField(max_length=50, verbose_name='Страна')
#     federal_district = models.CharField(max_length=50, verbose_name='Федеральный округ')
#     region_type = models.CharField(max_length=50, verbose_name='Тип региона')
#     region = models.CharField(max_length=50, verbose_name='Область')
#     area_type = models.CharField(max_length=50, verbose_name='Тип области')
#     area = models.CharField(max_length=50, verbose_name='Область')
#     city_type = models.CharField(max_length=50, verbose_name='Тип города')
#     city = models.CharField(max_length=20, verbose_name='Город')
#     settlement_type = models.CharField(max_length=50, verbose_name='Тип поселения')
#     settlement = models.CharField(max_length=50, verbose_name='Поселок')
#     kladr_id = models.CharField(max_length=50, verbose_name='Идентификатор кладра')
#
#     def __str__(self):
#         return self.city
#
#     class Meta:
#         verbose_name_plural = 'Опросы'
#         verbose_name = 'Опрос'
#         ordering = ['-published']
