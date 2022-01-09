from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #j
    from Bio.Seq import Seq

    F1 = 'TCTGGCCCAGTTCCTAGGTAGT'
    f1= Seq (F1) 
    
    from pydna.genbank import Genbank
    gb=Genbank("f.arabi68@yahoo.com")
   
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
