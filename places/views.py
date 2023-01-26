from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    features = []
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
                    "detailsUrl": reverse('place_number', args=(place.id, ))
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
    place = get_object_or_404(Place.objects.prefetch_related(), id=place_id)
    context = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={"ensure_ascii": False}
    )
