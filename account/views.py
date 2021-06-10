from django.shortcuts import render
from django.http import HttpResponse
#from .models import 
# Create your views here.

def login(request):
    return HttpResponse("<h1>HOME</h1>")

def logout(request):
    return HttpResponse("<h1>HOME</h1>")

def register(request):
    return render(request, 'account/register.html')

