from django.shortcuts import render
from .forms import AlbumsForm
from django.views import View
from django.contrib.auth.decorators import login_required


#Create your views here.

class create(View):
    form_class = AlbumsForm
    init ={'init':'init'}
    templateName ='CreateAlbums.html'
    def get(self,request):
        form =self.form_class(initial = self.init)
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(request,self.template_name,context)
        
        

