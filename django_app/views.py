from django.shortcuts import render
from django.http import HttpResponse

days = {
    'saturday':'this is saturday in dictionary',
    'sunday':'this is sunday in dictionary',
    'monday':'this is monday in dictionary',
    'tuesday':'this is tuesday in dictionary',
    'wednesday':'this is wednesday in dictionary',
    'thursday':'this is thursday in dictionary',
    'friday':'this is friday in dictionary',    
}

def aryan_http(request):
    return HttpResponse('i am in your app')

def aryan_dynamic(request , day):
    day_data = days.get(day)
    return HttpResponse(f'dynamic day is : {day} and dictionary data is {day_data}')
     