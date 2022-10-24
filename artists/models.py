from django.db import models


# Create your models here.
class Artists(models.Model):
    stageName = models.CharField(max_length = 50 ,unique = True)
    socialLinkField = models.URLField(null =False,blank  = True)
    def __str__(self):
        return(f" Name: "+self.stageName+f" Link: "+self.socialLinkField)
    def numberOfApprovedAlbums(self):
        return self.albums_set.filter(isApproved=True).count()


