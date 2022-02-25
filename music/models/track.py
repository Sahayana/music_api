from django.db import models

from music.models.base_model import BaseModel


class Track(BaseModel):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_play = models.DateTimeField()
