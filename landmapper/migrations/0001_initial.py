# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 00:51
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drawing', '0003_auto_20170623_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='AOI',
            fields=[
                ('aoi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='drawing.AOI')),
            ],
            options={
                'abstract': False,
            },
            bases=('drawing.aoi',),
        ),
        migrations.CreateModel(
            name='Taxlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_leng', models.FloatField(blank=True, null=True)),
                ('shape_area', models.FloatField(blank=True, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=3857, verbose_name='Grid Cell Geometry')),
            ],
            options={
                'verbose_name': 'Taxlot',
                'verbose_name_plural': 'Taxlots',
            },
        ),
    ]
