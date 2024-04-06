from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from newapp.models import *
import json
# class train_list:
#     route_no=0
#     train_no=0
#     from_location=0
#     to_location=0
#     arrival_time=0
#     departure_time=0
#     station_id=0
#     duration=0
def train(request):
    dict_data={}
    train_data={}
    from_loc=request.GET['from']
    to_loc=request.GET['to']
    date1=request.GET['date']
    train_data['cur_date']=date1
    print('cur_date1',date1)
    if from_loc==to_loc:
        dict_data['same_loc']=True
        return render(request,'home.html',dict_data)
    try:
        train_data['Location']=Route.objects.get(from_location=from_loc,to_location=to_loc)
        # print()
        train_data['train_available']=Route.objects.filter(from_location=from_loc,to_location=to_loc)
        for i in train_data['train_available']:
            # print(i.train_no.train_no)
            class_data=TrainClass.objects.filter(train_id=i.train_no)
            i.class_data=class_data
            for j in class_data:
                print(j.train_id.train_no,j.class_no.class_name)
                # train_check=Booking.objects.filter(train_id=i.train_no,date_of_journey='2024-04-04',class_no=j.class_no.class_type_id)
                train_check=Booking.objects.filter(train_id=i.train_no,date_of_journey=date1,class_no=j.class_no.class_type_id)
                
                j.available_seat=j.seat_end_range-j.seat_start_range+1-len(train_check)
                print(j.seat_end_range-j.seat_start_range+1-len(train_check))
            # for k in i.class_data.key():
            #     print(k)
                # for k in train_check:
                #     print(k.book_id)
        # train_check=Booking.objects.filter(train_id=1,date_of_journey='2024-04-04',class_no=1)
        # print(train_check)
        # for i in train_check:
        #     print(i.book_id)
    except:
        print('Error')
    return render(request,'train.html',train_data)
    # print(from_loc,to_loc,date1)
    # return render(request,'train.html')
# def book(request):
# my_django_view
#  book_id=models.BigAutoField(primary_key=True)
#     train_id=models.ForeignKey(Train,on_delete=models.CASCADE)
#     # seat_no=models.ForeignKey(Seat,on_delete=models.CASCADE)
#     seat_no=models.IntegerField()
#     route_id=models.ForeignKey(Route,on_delete=models.CASCADE)
#     user_id=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
#     date_of_journey=models.DateField()
#     class_no=models.ForeignKey(TrainClass,on_delete=models.CASCADE)
#  {'train_id': 1, 'seat_number': 3, 'route_id': 1, 'user_id': 1, 'date': 2024, 'class_id': 1}
# [06/Apr/2024 23:37:09] "POST /train/book/ HTTP/1.1" 200 41?
@csrf_exempt  # Disable CSRF protection for this view (for demonstration purposes)
def book(request):
    if request.method == 'POST':
        # Parse JSON data received from frontend
        try:
            data = json.loads(request.body)
            train_ob=Train.objects.get(train_no=data['train_id'])
            route_ob=Route.objects.get(route_no=data['route_id'])
            user_ob=Userdetail.objects.get(id=data['user_id'])
            trainclass_ob=TrainClass.objects.get(class_id=data['class_id'])
            datetime_object = datetime.strptime(data['date'], '%Y-%m-%d').date()
            bookmodel=Booking.objects.filter(train_id=data['train_id'],date_of_journey=datetime_object,seat_no=data['seat_number'])
            if len(bookmodel)==0:
                bookob=Booking()
                bookob.train_id=train_ob
                bookob.seat_no=data['seat_number']
                bookob.route_id=route_ob
                bookob.user_id=user_ob
                bookob.date_of_journey=datetime_object
                bookob.class_no=trainclass_ob
                bookob.save()
            print('Received data from frontend:', data)
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    # return render(request,'home.html')