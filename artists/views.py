from django.shortcuts import render
from .forms import ArtistsForm
from .models import Artists
from django.views import View

# Create your views here.
class create(View):
    form_class = ArtistsForm
    init ={'init':'init'}
    templateName ='CreateArtists.html'
    def get(self,request):
        form =self.form_class(initial = self.init)
        context = {'form':form}
        return render(request, self.templateName,context)

    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(request,self.templateName,context)

class List(View):
    def get(self,request):
        return render(request,'ListOfArtists.html',{'query_set': Artists.objects.all().prefetch_related('albums_set')})
