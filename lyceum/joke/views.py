from django.http import HttpResponse


def joke_index(request):
    response = HttpResponse("<body>Я чайник</body>")
    response.status_code = 418
    return response
