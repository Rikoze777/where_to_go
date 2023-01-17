from django.http import HttpResponse


def show_map(request):
    return HttpResponse('Здесь будет карта')
