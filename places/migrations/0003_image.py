# Generated by Django 3.0 on 2023-01-19 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20230119_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Фото')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Порядок')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='places.Place', verbose_name='Отношение к месту')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
