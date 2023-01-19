import json
from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def index(request):
    features = []
    detailsUrl = ["static/places/moscow_legends.json",
                  "/static/places/roofs24.json"]
    places = Place.objects.all()
    for place in places:
        feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.description_short,
                    "placeId": place.id,
                    "detailsUrl": detailsUrl[place.id-1]
                }
                }
        features.append(feature)

    context = {'places': {
                "type": "FeatureCollection",
                "features": features
                }
               }

    return render(request, "index.html", context=context)


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
    context = {
        "title": place.title,
        "imgs": [image.img.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return HttpResponse(
        json.dumps(context, ensure_ascii=False, indent=2),
        content_type="application/json"
    )
