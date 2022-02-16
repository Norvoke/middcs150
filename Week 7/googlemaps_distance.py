"""
CS150 class example
Demonstrates use of Google maps API
"""

import urllib.request
import json

METERS_PER_MILE = 1609.344

BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json?origin='

API_KEY = 'AIzaSyD3v69QTNiQ42spnRE5vbo1c3nhUSeVs9c'


def distance(src, dst):
    """
    Use Google maps api to determine distance.
    
    Distance is returned in miles between cities 'src' and 'dst'
    See https://developers.google.com/maps/documentation/directions/start
    
    Args:
        src: starting city (name or zip code) as a string
        dst: destination city (name or zip code) as a string
        
    Return:
        Distance in miles between src and dst cities
    
    """
    url =  BASE_URL + src + '&destination=' + dst + '&key=' + API_KEY
    with urllib.request.urlopen(url) as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
    pretty_print(contents)
    d = json.loads(contents)
    dist_meters = d['routes'][0]['legs'][0]['distance']['value']
    return int(dist_meters / METERS_PER_MILE)


def pretty_print(data):
    for d in data[:1000]:
        print(d, end='')
    print()

