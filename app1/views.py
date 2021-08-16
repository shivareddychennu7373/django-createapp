from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app1_function(request):
    return HttpResponse('<h1>this is app1_function</h1>')
def app1_function2(request):
    return HttpResponse('<h1>This is app1_function2,</h1>')