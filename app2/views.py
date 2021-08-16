from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2_function(request):
    return HttpResponse('<h1>This is app2_function</h1>')
