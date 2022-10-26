from django.shortcuts import render
from .forms import AlbumsForm

# Create your views here.
def index(request):
    form = AlbumsForm()
    if request.method =='POST':
       form = AlbumsForm(request.POST)
       if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request,'CreateAlbums.html',context)
