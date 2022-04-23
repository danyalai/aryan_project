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
    html_data = f'<h1>dynamic day is : {day} and dictionary data is {day_data}</h1>'
    return HttpResponse(html_data)
     
def days_list(request):
    days_list = list(days.keys())
    list_item = ""
    for day in days_list:
        list_item += f"<ul><li><a> {day} </a></li></ul>"
        
    return HttpResponse(list_item)