from django.db import models

# Create your models here.
class Userdetail(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Employee(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    dept=models.IntegerField()