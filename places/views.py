from django.shortcuts import render
from .models import Place


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
