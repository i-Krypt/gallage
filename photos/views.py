from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse
from .models import Image,Location

# Create your views here.
def index(request):
    return render(request, 'index.html')

def todays_photos(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-photos/todays-photos.html', {"date": date, "photos":photos})


def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_images = Image.objects.filter(category__category__icontains = search_term)
        message = f"{search_term}"
        print(searched_images)
        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message}) 


def location(request):
    locations =Location.objects.all()
    photos =Image.objects.all()

    context={
        'locations':locations,
        'photos':photos
    }
    return render(request, 'all-photos/locations.html',context)