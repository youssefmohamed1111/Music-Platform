from django.db import models

# Create your models here.
class Artists(models.Model):
    stageName = models.CharField(max_length = 50 ,unique = True)
    socialLinkField = models.URLField(null =False,blank  = True)
def __str__(self):
        return(" Name: "+self.stageName+" Link: "+self.socialLinkField)
