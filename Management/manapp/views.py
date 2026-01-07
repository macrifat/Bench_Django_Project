from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Home View')
def products(request):
    return HttpResponse('Products View')
def customer(request):
    return HttpResponse('Customer View')
    
