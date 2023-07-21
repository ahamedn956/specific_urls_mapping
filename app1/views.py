from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def bgmi(request):
    return HttpResponse('<h1>Winner Winner Chicken Dinner..........</h1>')
def ff(request):
    return HttpResponse('<h1><i>Booyah.........</i></h1>')

