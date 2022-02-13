from datetime import datetime
from django.shortcuts import render
from .models import Location

import  requests
# Create your views here.

def index(request):
    locations = Location.objects.all()
    data_to_display=[]
    weather_to_display=[]
    for location in locations:
        lat = location.location.x
        lon = location.location.y
        data = [lat,lon]
        data_to_display.append(data)
        url = 'https://api.weather.gov/points/{},{}'.format(round(lat,4),round(lon,4))
        grid_points = requests.get(url).json()
        grid_url = grid_points['properties']['forecast'] 
        weather =requests.get(grid_url).json()
        res = not bool(weather)
        if(res):
             weatherdata = {
                'name':grid_points['properties']['relativeLocation']['properties']['city'],
                'temperature':'Not Available at this Moment',
                'forecast':'Not Available'
            }
        else:
            weatherdata = {
                'name':grid_points['properties']['relativeLocation']['properties']['city'],
                'temperature':weather['properties']['periods'][1]['temperature'],
                'forecast':weather['properties']['periods'][1]['detailedForecast']
            }
        weather_to_display.append(weatherdata)
    context ={'data_to_display':data_to_display,'weather_to_display':weather_to_display}
    return render(request,'weather_leaflet/index.html',context)