import datetime as dt
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the Gallage.')

def todays_photos(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    
    return HttpResponse(html)

def convert_dates(dates):

    #function that gets the weekday number of the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    #Return the actual day of the week
    day = days[day_number]
    return day

    
    
# def home(request):
#     return render(request, 'home.html')