from django.db import models

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
