from django.contrib import admin
from .models import Artists
from . import models

# # Register your models here.



@admin.register(models.Artists)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stageName', 'socialLinkField','numberOfApprovedAlbums'] 