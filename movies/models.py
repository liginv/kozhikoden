from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from geoposition.fields import GeopositionField


class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=120)
    pic = models.ImageField(upload_to='movies/')

    NEW = "NEW"
    RUNNING = "RUN"
    STATUS = (
              (NEW, 'New'),
              (RUNNING, 'Running'),
              )
    status = models.CharField(max_length=3,
                              choices=STATUS,
                              default=NEW)

    ENGLISH = 'ENG'
    MALAYALAM = 'MAL'
    TAMIL = "TML"
    HINDI = "HID"
    LANGUAGE = (
        (ENGLISH, 'English'),
        (MALAYALAM, 'Malayalam'),
        (TAMIL, 'Tamil'),
        (HINDI, 'Hindi'),
    )
    language = models.CharField(max_length=3,
                                choices=LANGUAGE,
                                default=ENGLISH)

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=50, default=None)
    logo = models.ImageField(upload_to='theatre/', blank=True)
    landmark = models.CharField(max_length=100, default=None)
    location = GeopositionField()

    # http://mondeca.com/index.php/en/any-place-en

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Format: '+999999999'")
    contact_no = models.CharField(max_length=15,
                                  validators=[phone_regex],
                                  blank=False)  # validators should be a list

    ONLINE_AVA = 'Yes'
    ONLINE_NO = 'No'
    ONLINE_RESERVATION = (
                          (ONLINE_AVA, 'Yes'),
                          (ONLINE_NO, 'No'),
                          )
    online_reservation = models.CharField(max_length=3,
                                          choices=ONLINE_RESERVATION,
                                          default=ONLINE_AVA)
    link_to_reservation_site = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    hall = models.ForeignKey(Theatre, related_name="hall",
                             null=True, blank=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie)
    theatre = models.ForeignKey(Theatre)
    show_slug = models.SlugField()
    hall = models.ForeignKey(Hall, null=True, blank=True)

    class Meta:
        unique_together = ('movie', 'theatre', 'hall',)

    def __str__(self):
        return self.movie.name


class Time(models.Model):
    show = models.ForeignKey(Show, related_name='time')
    MORNING = 'Morning'
    NOON = 'Noon'
    EVENING = 'Evening'
    NIGHT = 'Night'

    TIME_CHOICES = (
                    ('Morning', (
                                ('9', '09:00 am'),
                                ('9:15', '09:15 am'),
                                ('9:30', '09:30 am'),
                                ('9:45', '09:45 am'),
                                ('10', '10:00 am'),
                                ('10:15', '10:15 am'),
                                ('10:30', '10:30 am'),
                                ('10:45', '10:45 am'),
                                ('11', '11:00 am'),
                                ('10:15', '10:15 am'),
                                ('11:30', '11:30 am'),
                                ('11:45', '11:45 am'), )),
                    ('Noon', (
                              ('12', '12:00 pm'),
                              ('12:15', '12:15 pm'),
                              ('12:30', '12:30 pm'),
                              ('12:45', '12:45 pm'),
                              ('1', '01:00 pm'),
                              ('1:15', '01:15 pm'),
                              ('1:30', '01:30 pm'),
                              ('1:45', '01:45 pm'),
                              ('2', '02:00 pm'),
                              ('2:15', '02:15 pm'),
                              ('2:30', '02:30 pm'),
                              ('2:45', '02:45 pm'),
                              ('3', '03:00 pm'),
                              ('3:15', '03:15 pm'),
                              ('3:30', '03:30 pm'),
                              ('3:45', '03:45 pm'), )),
                    ('Evening', (
                              ('4', '04:00 pm'),
                              ('4:15', '04:15 pm'),
                              ('4:30', '04:30 pm'),
                              ('4:45', '04:45 pm'),
                              ('5', '05:00 pm'),
                              ('5:15', '01:15 pm'),
                              ('5:30', '05:30 pm'),
                              ('5:45', '05:45 pm'),
                              ('6', '06:00 pm'),
                              ('6:15', '06:15 pm'),
                              ('6:30', '06:30 pm'),
                              ('6:45', '06:45 pm'),
                              ('7', '07:00 pm'),
                              ('7:15', '07:15 pm'),
                              ('7:30', '07:30 pm'),
                              ('7:45', '07:45 pm'), )),
                    ('Night', (
                              ('8', '08:00 pm'),
                              ('8:15', '08:15 pm'),
                              ('8:30', '08:30 pm'),
                              ('8:45', '08:45 pm'),
                              ('9', '09:00 pm'),
                              ('9:15', '09:15 pm'),
                              ('9:30', '09:30 pm'),
                              ('9:45', '09:45 pm'),
                              ('10', '10:00 pm'),
                              ('10:15', '10:15 pm'),
                              ('10:30', '10:30 pm'),
                              ('10:45', '10:45 pm'),
                              ('11', '11:00 pm'),
                              ('11:15', '11:15 pm'),
                              ('11:30', '11:30 pm'),
                              ('11:45', '11:45 pm'), )),
                    )
    time = models.CharField(max_length=100,
                            choices=TIME_CHOICES)
