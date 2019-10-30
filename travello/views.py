from django.shortcuts import render

from django.http import HttpResponse

from .models import Destination

# Create your views here.

def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = "The Indian City"
    dest1.price = 2000
    dest1.img = ''
    return render(request, 'index.html', {'dest1' : dest1})