from django.forms import ModelForm
from .models import Albums

class AlbumsForm(ModelForm):
    class Meta:
        model = Albums
        fields ='__all__'