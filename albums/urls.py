from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("create/", login_required(views.create.as_view())),
]
