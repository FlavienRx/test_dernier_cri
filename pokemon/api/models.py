from django.db import models
from django.utils.translation import gettext as _


class Type(models.Model):
    poke_api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        unique=True,
        max_length=64,
    )

    class Meta:
        ordering = ["poke_api_id"]


class Move(models.Model):
    poke_api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        unique=True,
        max_length=64,
    )

    class Meta:
        ordering = ["poke_api_id"]


class Pokemon(models.Model):
    poke_api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        unique=True,
        max_length=64,
    )
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    types = models.ManyToManyField(
        Type,
    )
    moves = models.ManyToManyField(
        Move,
    )
    small_image_url = models.URLField()
    large_image_url = models.URLField()

    class Meta:
        ordering = ["poke_api_id"]
