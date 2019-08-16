from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
from . models import Launch
from django.db import IntegrityError
import logging


def fetch(request):

    url = 'https://api.spacexdata.com/v3/launches'
    data = list()
    response = requests.get(url).json() #list

    for thing in response:
        s = thing['links']['mission_patch']
        if(s == None):
            s = "None"
        try :
            p = Launch(
                flight_number = thing['flight_number'],
                launch_date = datetime.strptime(thing['launch_date_utc'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                rocket_name = thing['rocket']['rocket_name'],
                mission_patch_link = s
            )
            p.save()
        except IntegrityError as e: 
            logging.error(e.args)
            """
            logging the integrity error or rather the error generated when duplicate 
            items are added to the database.
            This ensures that only one unique copy of each launch data remains
            """

        
    
    context = {
        'data' : Launch.objects.all(),
    }
    return render(request, 'task/home.html', context)

