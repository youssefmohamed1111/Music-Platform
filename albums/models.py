from django.db import models
from artists.models import Artists
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator

# Create your models here.
class Albums(TimeStampedModel) :
    Name = models.CharField(max_length = 50,default ="New",null= False,blank= False)
    releaseDateTime = models.DateTimeField(blank = False,null= False)
    cost = models.DecimalField(decimal_places= 4,max_digits=5)
    Artists = models.ForeignKey(Artists, on_delete = models.CASCADE)
    isApproved = models.BooleanField(default=True, help_text='Approve the album if its name is not explicit')
    
    def __str__(self):
        return(f" name: "+self.Name+" Creation Date and Time: "+self.created.strftime("%m/%d/%Y, %H:%M:%S")+" Release Date and Time: "+self.releaseDateTime.strftime("%m/%d/%Y, %H:%M:%S")+" cost: "+str(self.cost))

class Songs(models.Model):
    Albums = models.ForeignKey(Albums, on_delete=models.CASCADE)
    Name = models.CharField(max_length = 50,default ="Albums.Name")
    Image = models.ImageField(blank = False)
    image_thumbnail= ImageSpecField(source='Image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    Audio = models.FileField(blank=False, upload_to="audio/", validators=[
                             FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    def __str__(self):
        return(f" name: "+self.Name+" Image "+self.Image + "Image Thumbnail" + self.image_thumbnail + "Audio " + self.Audio)
    




