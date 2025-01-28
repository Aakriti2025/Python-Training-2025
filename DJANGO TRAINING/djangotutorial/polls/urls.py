from django.urls import path
import requests
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
]
