from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
   path("create/", views.create.as_view()),
    #path("", views.List.as_view()),
     path("", views.ArtistsList.as_view()),
]