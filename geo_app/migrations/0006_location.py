# Generated by Django 4.1.2 on 2022-10-22 09:43

from django.db import migrations, models
import django_admin_geomap


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0005_delete_city_alter_mymodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
    ]