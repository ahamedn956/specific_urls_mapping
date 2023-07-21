from django.urls import path
from app2.views import *

app_name='not'

urlpatterns=[
    path('Redbus/',Redbus,name='Redbus'),
    path('Bookmyshow/',Bookmyshow,name='Bookmyshow'),
]