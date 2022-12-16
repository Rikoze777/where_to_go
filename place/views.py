from django.shortcuts import render
from place.models import Place, Image
from django.urls import reverse


def index(request):
    features = []
    all_places = Place.objects.all()
    for place in all_places:
        feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "1"
                },
        }
        features.append(feature)

    context = {
        "saved_places": {
            "type": "FeatureCollection",
            "features": features,
        },
    }
    return render(request, "index.html", context=context)
