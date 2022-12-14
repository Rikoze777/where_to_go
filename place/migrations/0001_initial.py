# Generated by Django 3.0 on 2022-12-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Полное описание')),
                ('lng', models.FloatField(verbose_name='Долота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
