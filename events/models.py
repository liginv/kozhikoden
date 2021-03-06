from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from geoposition.fields import GeopositionField


class Event(models.Model):
    name = models.CharField(max_length=50)
    organiser = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='events/',
                            default='default/events.png')
    date = models.DateField()
    starting_time = models.TimeField()
    fee = models.IntegerField()

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Format: '+999999999'")
    contact_no = models.CharField(max_length=15,
                                  validators=[phone_regex],
                                  blank=False)  # validators should be a list
    location = GeopositionField()

    def __str__(self):
        return self.name
