from django.core import validators
from django.db import models

from my_plant_app.plant_app.validators import validate_name_capital_letter


# Create your models here.

class Profile(models.Model):
    MAX_LEN_USER = 10
    MAX_LEN_FIRST_NAME = 20
    MAX_LEN_LAST_NAME = 20
    MIN_LEN_USER = 2

    username = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_USER,
        validators=(validators.MinLengthValidator(MIN_LEN_USER),),
        verbose_name='Username',
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validate_name_capital_letter,),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_LAST_NAME,
        validators=(validate_name_capital_letter,),
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(blank=True, null=True, verbose_name='Profile picture')


class Plant(models.Model):

    class Meta:
        ordering = ['pk']

    MAX_LEN_TYPE = 14
    MAX_LEN_NAME = 20
    MIN_LEN_NAME = 2

    TYPES = [
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    ]

    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_TYPE,
        choices=TYPES,
        verbose_name='Type'
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_NAME,
        validators=(validators.MinLengthValidator(MIN_LEN_NAME), validate_name_capital_letter),
    )

    image_url = models.URLField(blank=False, null=False,verbose_name='Image Url')

    description = models.TextField(blank=False, null=False, )

    price = models.FloatField(blank=False, null=False, validators=(validators.MinValueValidator(0.0),))
