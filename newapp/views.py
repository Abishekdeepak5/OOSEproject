from django.shortcuts import render
from django.http import HttpResponse
from .models import Userdetail
from train.models import *
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Hello world</h1><h5>Hello world</h5>')
    # trainobj=Train()
    data=Route.objects.all()
    return render(request,'home.html',{'trains':data})
def register(request):
    if request.method=='POST':
        ob=Userdetail()
        ob.username=request.POST['name']
        ob.email=request.POST['email']
        ob.password=request.POST['password']
        ob.save()
    data=Userdetail.objects.all()
    return render(request,'register.html',{'datas':data})
def login(request):
    if request.method=='POST':
        user_email=request.POST['email']
        user_password=request.POST['password']
        try:
            data=Userdetail.objects.get(email=user_email,password=user_password)
            return render(request,'home.html',{'user':data})
        except:
            return render(request,'login.html',{'data':"Invalid Email or Password"})
    return render(request,'login.html')