from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start_game", views.start_game, name="start_game"),
]