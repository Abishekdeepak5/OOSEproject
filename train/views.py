from django.shortcuts import render
from .models import *
from datetime import datetime
def train(request):
    dict_data={}
    train_data={}
    from_loc=request.GET['from']
    to_loc=request.GET['to']
    date1=request.GET['date']
    train_data['cur_date']=date1
    if from_loc==to_loc:
        dict_data['same_loc']=True
        return render(request,'home.html',dict_data)
    try:
        train_data['Location']=Route.objects.get(from_location=from_loc,to_location=to_loc)
        # print()
        train_data['train_available']=Route.objects.filter(from_location=from_loc,to_location=to_loc)
        for i in train_data['train_available']:
            print(i.train_no.train_no)
            class_data=TrainClass.objects.filter(train_id=i.train_no)
            train_class=[]
            for j in class_data:
                print(j.class_id.class_name)
                train_class.append(j.class_id.class_name)
            print(train_class)
            train_data[i.train_no.train_no]=train_class
            print(train_data[i.train_no.train_no])
    except:
        print('Error')
    return render(request,'train.html',train_data)
    # print(from_loc,to_loc,date1)
    # return render(request,'train.html')