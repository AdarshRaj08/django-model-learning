from django.shortcuts import render,HttpResponse
from .models import Studentm

# Create your views here.

def manager(request):
    # st = Studentm.adarsh.all()
    st = Studentm.objects.all()

    print(st)
    return HttpResponse("this is page manager")