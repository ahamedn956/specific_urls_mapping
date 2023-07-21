from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Redbus(request):
    return HttpResponse('<h1>your ticket from bangalore to chennai is confirmed!!!!!</h1>')
def Bookmyshow(request):
    return HttpResponse('<h1><i>Tickets for baby Movie is successfully Booked!!!!!</i></h1>')

