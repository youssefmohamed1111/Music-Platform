from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
class Login(View):
    templateName ='login.html'
    init ={'init':'init'}
    def get(self,request):
        return render(request,self.templateName,{})
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/artists/create')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/artists/')

