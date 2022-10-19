# Generated by Django 4.1.2 on 2022-10-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0002_alter_city_geo_lat_alter_city_geo_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='block',
            field=models.CharField(max_length=50, null=True, verbose_name='Блок дома'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=20, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=50, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='city',
            name='federal_district',
            field=models.CharField(max_length=50, null=True, verbose_name='Федеральный округ'),
        ),
        migrations.AlterField(
            model_name='city',
            name='flat',
            field=models.CharField(max_length=50, null=True, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='city',
            name='geo_lat',
            field=models.CharField(max_length=50, null=True, verbose_name='Географическая широта'),
        ),
        migrations.AlterField(
            model_name='city',
            name='geo_lon',
            field=models.CharField(max_length=50, null=True, verbose_name='Географическая долгота'),
        ),
        migrations.AlterField(
            model_name='city',
            name='house',
            field=models.CharField(max_length=50, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.CharField(max_length=50, null=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='city',
            name='street',
            field=models.CharField(max_length=50, null=True, verbose_name='Улица'),
        ),
    ]
