from .models import Albums
from django.contrib import admin
from . import models
# Register your models here.
class AlbumsInline(admin.TabularInline):
    model = models.Albums
    


@admin.register(models.Albums)
class AlbumsAdmin(admin.ModelAdmin):
  list_display = [ 'Name', 'releaseDateTime',
                    'cost','Artists', 'isApproved']
  readonly_fields = ['created']