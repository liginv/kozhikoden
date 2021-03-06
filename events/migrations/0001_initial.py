# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 17:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('organiser', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='events/')),
                ('date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('fee', models.IntegerField()),
                ('contact_no', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Format: '+999999999'", regex='^\\+?1?\\d{9,15}$')])),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
