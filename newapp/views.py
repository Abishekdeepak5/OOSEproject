from django.shortcuts import render
from django.http import HttpResponse
from .models import Userdetail
from train.models import *
from django import forms
from .forms import MyForm
from datetime import datetime
# Create your views here.
class TrainAvailable:
    from_loc=""
    to_loc=""
    train_name=""
def home(request):
    data=Route.objects.all()
    place=Place.objects.all()
    dict_data={'places':place}
    dict_data['cur_date']=datetime.now()
    dict_data['seatType']=ClassType.objects.all()
    # if request.method=='POST':
    #     from_loc=request.POST['from']
    #     to_loc=request.POST['to']
    #     date1=request.POST.get('date')
    #     input_datetime = datetime.strptime(date1, "%Y-%m-%d")
    #     output_date_string = input_datetime.strftime("%a, %d %b %Y")
    #     train_data={}
    #     train_data['Date']=output_date_string
    #     try:
    #         train_data['Location']=Route.objects.get(from_location=from_loc,to_location=to_loc)
    #         train_data['train_available']=Route.objects.filter(from_location=from_loc,to_location=to_loc)
    #     except:
    #         pass
    #     if from_loc==to_loc:
    #         dict_data['same_loc']=True
    #         return render(request,'home.html',dict_data)
    #     return render(request,'train.html',train_data)
    return render(request,'home.html',dict_data)
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