from django.contrib import admin
from .models import Artists
from albums.admin import AlbumsInline
from . import models

# # Register your models here.



@admin.register(models.Artists)
class ArtistAdmin(admin.ModelAdmin):
   # inlines = [AlbumsInline]
    list_display = ['stageName', 'socialLinkField','numberOfApprovedAlbums'] 