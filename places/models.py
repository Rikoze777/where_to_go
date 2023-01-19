from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Место', max_length=200, unique=True)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title
