from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from geoposition.fields import GeopositionField


class Restaurent(models.Model):
    restaurent_name = models.CharField(max_length=50)
    restaurent_pic = models.ImageField(upload_to='restaurents/')

    VEG = "VEG"
    NON_VEG = "NON"
    BOTH = "BTH"
    FOOD_TYPE = (
              (VEG, 'Veg'),
              (NON_VEG, 'Non-Veg'),
              (BOTH, 'Veg & Non-Veg'),
              )
    food_type = models.CharField(max_length=3,
                                 choices=FOOD_TYPE,
                                 default=BOTH)

    opening_time = models.IntegerField(default=None)
    closing_time = models.IntegerField(default=None)

    NAADAN = 'NAD'
    ARABIAN = 'ARB'
    BEACH = 'BEH'
    CHILL_OUT = 'CHI'
    STANDARD = 'STD'
    AMBIENCE = (
        (STANDARD, 'Standard'),
        (NAADAN, 'Naadan'),
        (ARABIAN, 'Arabian'),
        (BEACH, 'Beach'),
        (CHILL_OUT, 'Chill-Out'),
    )
    ambience = models.CharField(max_length=3,
                                choices=AMBIENCE,
                                default=STANDARD)

    YES = "YES"
    NO = "NO"
    HOME_DELIVERY = (
              (YES, 'Yes'),
              (NO, 'No'),
              )
    home_delivery = models.CharField(max_length=3,
                                     choices=HOME_DELIVERY,
                                     default=NO)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Format: '+999999999'")
    contact_no = models.CharField(max_length=15,
                                  validators=[phone_regex],
                                  blank=False)  # validators should be a list
    location = GeopositionField()

    def __str__(self):
        return self.restaurent_name
