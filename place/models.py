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
    place = models.ForeignKey(
        'Place',
        verbose_name='Место',
        related_name='images',
        on_delete=models.SET_NULL,
        null=True)
    img = models.ImageField(
        'Картинка',
        upload_to='',
        null=True,
        blank=True)
    img_title = models.CharField(
        'Название',
        max_length=50,
        null=True,
        unique=True,
        )
    order = models.PositiveIntegerField('Порядок', default=1)

    class Meta:
        ordering = ['order']
