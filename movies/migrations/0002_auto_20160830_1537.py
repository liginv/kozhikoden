# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pic',
            field=models.ImageField(default='default/movie.png', upload_to='movies/'),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='logo',
            field=models.ImageField(default='default/theatre.png', upload_to='theatre/'),
        ),
    ]
