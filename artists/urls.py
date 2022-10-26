from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.index),
    path("", views.showList),
]