from django.urls import path, re_path, register_converter

from catalog import converters, views

register_converter(converters.PositiveInteger, "int+")
app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="home"),
    re_path(r"^re/[1-9]\d*$", views.regex_page_view),
    path("<int:pk>", views.item_detail),
    path("converter/<int+:pk>", views.item_detail),
]
