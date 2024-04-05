from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Place)
admin.site.register(ClassType)
admin.site.register(TrainClass)
admin.site.register(Seat)
admin.site.register(Booking)



