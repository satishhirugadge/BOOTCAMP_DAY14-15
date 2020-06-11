from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def met1(request):
    return HttpResponse("Hello my name is Satish!!!")

def met2(request):
    return render(request , "Bootapp/home.html")

def met3(request):
    return render(request , "Bootapp/index.html")


