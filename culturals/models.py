from __future__ import unicode_literals
from django.db import models
from geoposition.fields import GeopositionField


class Cultural(models.Model):
    event_name = models.CharField(max_length=50)
    main_attraction = models.CharField(max_length=50)
    cultural_pic = models.ImageField(upload_to='cults/')

    EXIBITION = 'EXPO'
    GAUZAL = 'GUZ'
    DRAMA = 'DRM'
    MUSIC = 'MUS'
    TYPE = (
        (EXIBITION, 'Expo'),
        (GAUZAL, 'Gauzal Night'),
        (DRAMA, 'Drama'),
        (MUSIC, 'Music'),
    )
    event_type = models.CharField(max_length=3,
                                  choices=TYPE,
                                  default=EXIBITION)
    location = GeopositionField()
