from django.urls import path
from app1.views import *
 
app_name = 'something'

urlpatterns =[
    path('bgmi/',bgmi,name='bgmi'),
    path('ff/',ff,name='ff'),
]
