from django.shortcuts import render,HttpResponse
from .models import Student,Contractor,Teacher
# Create your views here.

def home(request):
    st = Student.objects.all()
    tt = Student.objects.all()
    ct = Student.objects.all()

    print(st)
    return HttpResponse("hii")