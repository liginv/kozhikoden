# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culturals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultural',
            name='pic',
            field=models.ImageField(default='default/culturals.png', upload_to='cults/'),
        ),
    ]