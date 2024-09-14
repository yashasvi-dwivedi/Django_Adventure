from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "newyear/index.html" , {
        "newyear" : datetime.now == 1 and datetime.now == 1
    })