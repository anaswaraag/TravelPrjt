from django.shortcuts import render
from . models import  Place
from . models import Team

def index(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()

    return render(request,"index.html",{'result':obj,'data':obj1})

# Create your views here.

