# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_attraction', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='cults/')),
                ('event_type', models.CharField(choices=[('EXPO', 'Expo'), ('GUZ', 'Gauzal Night'), ('DRM', 'Drama'), ('MUS', 'Music')], default='EXPO', max_length=5)),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
