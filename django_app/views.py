from django.shortcuts import render
from django.http import HttpResponse

def aryan_http(request):
    return HttpResponse('i am in your app')

def aryan_dynamic(request , days):
    return HttpResponse(days)
    