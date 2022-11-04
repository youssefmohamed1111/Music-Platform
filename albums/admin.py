from .models import Albums,Songs
from django.contrib import admin
from . import models
# Register your models here.

class SongsInline(admin.StackedInline):
    model = models.Songs
    min_num = 1
    extra =0
   
@admin.register(models.Albums)
class AlbumsAdmin(admin.ModelAdmin):
  inlines = [SongsInline]
  list_display = [ 'Name', 'releaseDateTime',
                    'cost','Artists', 'isApproved']
  readonly_fields = ['created']
@admin.register(models.Songs)
class SongsAdmin(admin.ModelAdmin):
  list_display = [ 'Albums','Name', 'Image',
                    'image_thumbnail','Audio']
