from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('app1/',app1_function,name='app1'),
    path('app12/',app1_function2,name='app1')
    
]