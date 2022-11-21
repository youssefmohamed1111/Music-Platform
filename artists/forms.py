from django.forms import ModelForm
from .models import Artists

class ArtistsForm(ModelForm):
    class Meta:
        model = Artists
        fields ='__all__'