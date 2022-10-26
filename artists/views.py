from django.shortcuts import render
from .forms import ArtistsForm
from .models import Artists

# Create your views here.
def index(request):
    form = ArtistsForm()
    if request.method =='POST':
       form = ArtistsForm(request.POST)
       if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request,'CreateArtists.html',context)
def showList(request):
    return render(request,'ListOfArtists.html',{'query_set': Artists.objects.all().prefetch_related('albums_set')})