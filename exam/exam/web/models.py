from django.core import validators
from django.db import models

from exam.web.validators import validate_first_letter, validate_fruit_name


# Create your models here.
class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 25

    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1

    MAX_LEN_EMAIL = 40

    MIN_LEN_PASSWORD = 8
    MAX_LEN_PASSWORD = 20

    DEFAULT_AGE = 18

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validate_first_letter, validators.MinLengthValidator(MIN_LEN_FIRST_NAME)),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_LAST_NAME,
        validators=(validate_first_letter, validators.MinLengthValidator(MIN_LEN_LAST_NAME)),
        verbose_name='Last Name',
    )

    email = models.EmailField(blank=False, null=False, max_length=MAX_LEN_EMAIL)

    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_PASSWORD,
        validators=(validators.MinLengthValidator(MIN_LEN_PASSWORD),),
    )

    image_url = models.URLField(blank=True, null=True, verbose_name='Image URL')

    age = models.PositiveIntegerField(blank=True, null=True, default=DEFAULT_AGE)


class Fruit(models.Model):
    class Meta:
        ordering = ['pk']

    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30

    name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LEN_NAME,
        validators=(validate_fruit_name, validators.MinLengthValidator(MIN_LEN_NAME)),
    )  # required

    image_url = models.URLField(blank=False, null=False, verbose_name='Image URL')  # required

    description = models.TextField(blank=False, null=False)  # required

    nutrition = models.TextField(blank=True, null=True)  # optional
