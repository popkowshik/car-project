from django.shortcuts import render

# Create your views here.

import json

file = open(r'C:\Users\kowsh\OneDrive\Desktop\django\car assignment\app1\cars.json','r')
json_data = file.read()
py_data = json.loads(json_data)

cars = py_data['cars']

def home_cars(request):
    context = {
        'cars':cars 
    }

    return render(request,'home_cars.html',context)

def one_car(request,id):
    context = {
        'car':cars[id-1]
    }

    return render(request,'one_car.html',context)

def home(request):
    return render(request,'home_cars.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')