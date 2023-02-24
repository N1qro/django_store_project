from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробнее об элементе: {pk}</body>")


def regex_page_view(request):
    return HttpResponse("<body>Вы ввели целое положительное число!</body>")
