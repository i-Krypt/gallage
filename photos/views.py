from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    return render(request, 'index.html')

def todays_photos(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-photos/todays-photos.html', {"date": date, "photos":photos})

def convert_dates(dates):

    #function that gets the weekday number of the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    #Return the actual day of the week
    day = days[day_number]
    return day

    
    
# def home(request):
#     return render(request, 'home.html')