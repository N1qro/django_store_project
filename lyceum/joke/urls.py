from django.urls import path

from . import views


urlpatterns = [
    path("", views.joke_index),
]
