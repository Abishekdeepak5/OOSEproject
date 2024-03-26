from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from newapp.models import *
# Create your views here.

class UserApi(APIView):
    def get(self,request):
        usermodel=Userdetail.objects.all().values()
        return Response({'Users':usermodel})
    
    def post(self,request):
        Userdetail.objects.create(username=request.data['username'],
                                  password=request.data['password'],
                                  email=request.data['email'])
        # usermodel=Userdetail.objects.all().filter(id=request.data["id"]).values()

        return Response({'user Added'})
