from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    extras = {'name':'Arafat', 'place':'Bangladesh' }
    return render(request, 'index.html', extras)
    #return HttpResponse("<h1>HOME</h1>")