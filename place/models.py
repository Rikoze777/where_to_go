from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Заголовок')
    description_short = models.TextField(blank=True,
                                         verbose_name='Краткое описание')
    description_long = models.TextField(blank=True,
                                        verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Место')
    image = models.ImageField(verbose_name='Картинки',
                              upload_to=f'{Place.title}/')

    def __str__(self):
        return self.place
