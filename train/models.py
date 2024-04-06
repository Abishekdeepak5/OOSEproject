from django.db import models
from newapp.models import *
# Create your models here.
class Train(models.Model):
    train_no=models.BigAutoField(primary_key=True)
    train_name=models.CharField(max_length=30)
    capacity=models.IntegerField()

class Station(models.Model):
    station_id=models.BigAutoField(primary_key=True)
    station_name=models.CharField(max_length=30)
    station_location=models.CharField(max_length=100)


class Place(models.Model):
    place_id=models.BigAutoField(primary_key=True)
    place_name=models.CharField(max_length=30)

class Route(models.Model):
    route_no=models.BigAutoField(primary_key=True)
    train_no=models.ForeignKey(Train,on_delete=models.CASCADE)
    from_location=models.ForeignKey(Place,on_delete=models.CASCADE, related_name='routes_from')
    to_location=models.ForeignKey(Place,on_delete=models.CASCADE, related_name='routes_to')
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    station_id=models.ForeignKey(Station,on_delete=models.CASCADE)
    duration=models.TimeField()

class ClassType(models.Model):
    class_type_id=models.BigAutoField(primary_key=True)
    class_name=models.CharField(max_length=30)

class TrainClass(models.Model):
    class_id=models.BigAutoField(primary_key=True)
    train_id=models.ForeignKey(Train,on_delete=models.CASCADE)
    class_no=models.ForeignKey(ClassType,on_delete=models.CASCADE)
    price=models.IntegerField(default=250)
    seat_start_range=models.IntegerField()
    seat_end_range=models.IntegerField()

class Seat(models.Model):
    seat_id=models.BigAutoField(primary_key=True)
    train_id=models.ForeignKey(Train,on_delete=models.CASCADE)
    seat_type=models.ForeignKey(TrainClass,on_delete=models.CASCADE)
    seat_number=models.IntegerField()

class Booking(models.Model):
    book_id=models.BigAutoField(primary_key=True)
    train_id=models.ForeignKey(Train,on_delete=models.CASCADE)
    # seat_no=models.ForeignKey(Seat,on_delete=models.CASCADE)
    seat_no=models.IntegerField()
    route_id=models.ForeignKey(Route,on_delete=models.CASCADE)
    user_id=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    date_of_journey=models.DateField(null=True)
    class_no=models.ForeignKey(TrainClass,on_delete=models.CASCADE)
