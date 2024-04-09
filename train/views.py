from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from newapp.models import *
import json
def train(request):
    dict_data={}
    train_data={}
    from_loc=request.GET['from']
    to_loc=request.GET['to']
    date1=request.GET['date']
    seat_type=request.GET['seat']
    train_data['cur_date']=date1
    if from_loc==to_loc:
        place=Place.objects.all()
        dict_data={'places':place}
        dict_data['same_loc']=True
        return render(request,'home.html',dict_data)
    try:
        # train_data['Location']=Route.objects.get(from_location=from_loc,to_location=to_loc)
        train_data['train_available']=Route.objects.filter(from_location=from_loc,to_location=to_loc)
        train_data['Location']=train_data['train_available'].first()
        for i in train_data['train_available']:
            class_data=TrainClass.objects.filter(train_id=i.train_no)
            i.class_data=class_data
            for j in class_data:
                train_check=Booking.objects.filter(train_id=i.train_no.train_no,date_of_journey=date1,class_no=j.class_id)
                j.available_seat=j.seat_end_range-j.seat_start_range+1-len(train_check)
    except Exception as e:
        print('Error',e)
    return render(request,'train.html',train_data)
    
@csrf_exempt 
def book(request):
    if request.method == 'POST':
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
                return JsonResponse({'user_id':bookob.user_id.id,'route_id':bookob.route_id.route_no,'book_id':bookob.pk,'seat_no':bookob.seat_no})
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def ticket(request):
    # var url = `ticket/?user_id=${userId}&book_id=${bookId}&seat_no=${seatNo}&route_id=${routeId}
    ticket_data={}
    user_id = request.GET.get('user_id')
    book_id = request.GET.get('book_id')
    ticket_data['seat_no']=request.GET.get('seat_no')
    routeId=request.GET.get('route_id')

    userob=Userdetail.objects.get(id=user_id)
    bookob=Booking.objects.get(book_id=book_id)
    routeob=Route.objects.get(route_no=routeId)
    ticket_data['userob']=Userdetail.objects.get(id=user_id)
    ticket_data['bookob']=Booking.objects.get(book_id=book_id)
    ticket_data['routeob']=Route.objects.get(route_no=routeId)
    return render(request,'ticket.html',ticket_data)