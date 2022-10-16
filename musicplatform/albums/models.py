from django.db import models
from artists.models import Artist

# Create your models here.
class Albums(models.Model):
    Name = models.CharField(default ="New")
    creationDateTime = models.DateTimeField()
    releaseDateTime = models.DateTimeField(blank = False)
    cost = models.DecimalField()
    Artist = models.ForeignKey(to, on_delete = models.CASCADE)


