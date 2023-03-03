from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = "homepage/index.html"
    context = {}
    return render(request, template, context)


def joke_index(request):
    response = HttpResponse("<body>Я чайник</body>")
    response.status_code = 418
    return response
