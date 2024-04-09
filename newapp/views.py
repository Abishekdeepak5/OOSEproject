from django.shortcuts import render
from django.http import HttpResponse
from .models import Userdetail
from train.models import *
from django import forms
from .forms import MyForm
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
    return render(request,'home.html',dict_data)
def register(request):
    if request.method=='POST':
        ob=Userdetail()
        ob.username=request.POST['name']
        ob.email=request.POST['email']
        ob.password=request.POST['password']
        ob.save()
        return render(request,'login.html')
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
@csrf_exempt 
def saveuser(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            email=data['email']
            password=data['password']
            user=Userdetail.objects.get(email=email,password=password)
            return JsonResponse({'user_id':user.id})
        except:
            return JsonResponse({'error':'error'})
        return JsonResponse({'msg':'Hello'})
    return JsonResponse({'msg':'Hello'})