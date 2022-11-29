from django.shortcuts import render


def startpage(request):
    return render(request, 'index.html')
