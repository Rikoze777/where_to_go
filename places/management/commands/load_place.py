from django.core.management.base import BaseCommand
import requests
from places.models import Place, Image
from django.core.files.base import ContentFile
import os


class Command(BaseCommand):
    help = 'Load information about places into DB'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='json link')

    def fetch_imgs(self, place, links):
        for number, link in enumerate(links):
            try:
                response = requests.get(link)
                response.raise_for_status()
                head_url, ext = os.path.splitext(link)
                img = ContentFile(
                    response.content,
                    name=f"{place.title}_{number}{ext}",
                )
                Image.objects.create(place=place, img=img)
            except requests.exceptions.HTTPError as error:
                self.stderr.write(self.style.ERROR(
                    f'Image loading {error}'))
                continue

    def handle(self, *args, **options):
        link = options['link']
        try:
            response = requests.get(link)
            response.raise_for_status()
            payload = response.json()
            img_links = payload['imgs']

            place, created = Place.objects.get_or_create(
                title=payload['title'],
                defaults={
                    'description_short': payload['description_short'],
                    'description_long': payload['description_long'],
                    'lng': payload['coordinates']['lng'],
                    'lat': payload['coordinates']['lat']
                }
            )
            if not created:
                self.stdout.write(
                    self.style.WARNING('JSON already in DB.')
                )
                return

        except requests.exceptions.HTTPError as error:
            self.stderr.write(self.style.ERROR(
                f'JSON load {error}'))
            return

        self.fetch_imgs(place, img_links)
        self.stdout.write(self.style.SUCCESS(f'{place.title} succesfully added'))
