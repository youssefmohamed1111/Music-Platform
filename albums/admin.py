from .models import Albums,Songs
from django.contrib import admin
from . import models
# Register your models here.
class AlbumsInline(admin.TabularInline):
    model = models.Albums
class SongsInline(admin.StackedInline):
    model = models.Songs
    extra =0
    min_num = 1
    


@admin.register(models.Albums)
class AlbumsAdmin(admin.ModelAdmin):
  inlines = [SongsInline]
  list_display = [ 'Name', 'releaseDateTime',
                    'cost','Artists', 'isApproved']
  readonly_fields = ['created']
@admin.register(models.Songs)
class SongsAdmin(admin.ModelAdmin):
  list_display = [ 'Name', 'Image',
                    'image_thumbnail','Audio']
