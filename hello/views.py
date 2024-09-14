from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def yash(request):
    return HttpResponse("Hello, Yash!")

def home(request):
    return HttpResponse("Hello, Home!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })