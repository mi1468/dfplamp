from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'./index.html')

def webpage2(request):
    return render(request,'index2.html')