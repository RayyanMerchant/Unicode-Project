from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json

def fetch(request):

    url = 'https://api.spacexdata.com/v3/launches'
    data = list()
    response = requests.get(url).json() #list

    for thing in response:
        data.append({'flight_number' : thing['flight_number'], 
        'launch_date' : datetime.strptime(thing['launch_date_utc'], '%Y-%m-%dT%H:%M:%S.%fZ'),
        'rocket_name' : thing['rocket']['rocket_name'],
        'mission_patch_link' : thing['links']['mission_patch']
        })
        
    """
    passing the list of dictionaries containing the data to the html template
    so that it can be displayed on the home page
    """
    context = {
        'data' : data,
    }
    return render(request, 'task/home.html', context)

