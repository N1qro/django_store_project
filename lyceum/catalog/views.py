from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    template = "catalog/catalog.html"
    context = {}
    return render(request, template, context)


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробнее об элементе: {pk}</body>")


def regex_page_view(request):
    return HttpResponse("<body>Вы ввели целое положительное число!</body>")
