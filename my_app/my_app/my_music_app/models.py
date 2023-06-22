from enum import Enum

from django.core import validators
from django.db import models

from my_app.my_music_app.validators import validate_only_alnum_and_underscore


# Create your models here.


class Profile(models.Model):
    MIN_LEN_USER = 2
    MAX_LEN_USER = 15

    username = models.CharField(max_length=MAX_LEN_USER,
                                validators=(
                                    validators.MinLengthValidator(MIN_LEN_USER),
                                    validate_only_alnum_and_underscore), )

    email = models.EmailField(null=False, blank=False, )
    age = models.PositiveIntegerField(null=True, blank=True, )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.value, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        ),
    )

    class Meta:
        ordering = ('pk',)