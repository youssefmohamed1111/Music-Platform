from django.db import models
from artists.models import Artists

# Create your models here.
class Albums(models.Model):
    Name = models.CharField(max_length = 50,default ="New")
    creationDateTime = models.DateTimeField()
    releaseDateTime = models.DateTimeField(blank = False)
    cost = models.DecimalField(decimal_places= 4,max_digits=5)
    Artists = models.ForeignKey(Artists, on_delete = models.CASCADE)
    isApproved = models.BooleanField(default=True, help_text='Approve the album if its name is not explicit')
    
    def __str__(self):
        return(f" name: "+self.Name+" Creation Date and Time: "+self.creationDateTime.strftime("%m/%d/%Y, %H:%M:%S")+" Release Date and Time: "+self.releaseDateTime.strftime("%m/%d/%Y, %H:%M:%S")+" cost: "+str(self.cost))




