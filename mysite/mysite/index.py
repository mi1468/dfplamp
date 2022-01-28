from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    x = "salam"
    y = " khobam :))"
    y += x


    return render(request,'./index.html' ,{'data':y} )

def webpage2(request):
    return render(request,'index2.html')