from django.db import models
from artists.models import Artists
from model_utils.models import TimeStampedModel

# Create your models here.
class Albums(TimeStampedModel) :
    Name = models.CharField(max_length = 50,default ="New")
    #creationDateTime = models.DateTimeField()
    releaseDateTime = models.DateTimeField(blank = False)
    cost = models.DecimalField(decimal_places= 4,max_digits=5)
    Artists = models.ForeignKey(Artists, on_delete = models.CASCADE)
    isApproved = models.BooleanField(default=True, help_text='Approve the album if its name is not explicit')
    
    def __str__(self):
        return(f" name: "+self.Name+" Creation Date and Time: "+self.created.strftime("%m/%d/%Y, %H:%M:%S")+" Release Date and Time: "+self.releaseDateTime.strftime("%m/%d/%Y, %H:%M:%S")+" cost: "+str(self.cost))




