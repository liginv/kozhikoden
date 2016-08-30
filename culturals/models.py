from __future__ import unicode_literals
from django.db import models
from geoposition.fields import GeopositionField


class Cultural(models.Model):
    name = models.CharField(max_length=50)
    main_attraction = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='cults/',
                            default='default/culturals.png')

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
    event_type = models.CharField(max_length=5,
                                  choices=TYPE,
                                  default=EXIBITION)
    location = GeopositionField()

    def __str__(self):
        return self.name
