# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 17:22
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
            name='Restaurent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='restaurents/')),
                ('food_type', models.CharField(choices=[('VEG', 'Veg'), ('NON', 'Non-Veg'), ('BTH', 'Veg & Non-Veg')], default='BTH', max_length=3)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('ambience', models.CharField(choices=[('STD', 'Standard'), ('NAD', 'Naadan'), ('ARB', 'Arabian'), ('BEH', 'Beach'), ('CHI', 'Chill-Out')], default='STD', max_length=3)),
                ('home_delivery', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=3)),
                ('contact_no', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Format: '+999999999'", regex='^\\+?1?\\d{9,15}$')])),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
