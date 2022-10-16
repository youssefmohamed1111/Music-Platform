from django.db import models

# Create your models here.
class Artists(models.Model):
    stageName = models.CharField(max_length = 50 ,unique = True)
    socialLinkField = models.URLField(null =False,blank  = true)
