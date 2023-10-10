"""
Report the current weather from the web for a zip code

CS 150 Lab 7

Name: Finn Ellingwood
Section: B

Creativity:
"""

import sys
import urllib.request
import json


BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?zip='

API = '64e3ee7a4b540e2c7591e68d94c9e664'

def create_url(zip_code):
    url = str((BASE_URL + zip_code + ',us&APPID=' + API + '&units=imperial'))
    return url

def print_usage():
    print('Usage: python3 lab7_weather.py <5-digit zip code>')

def get_temperature(zip_code):
    """
    Look uo the current temperature at openweathermap for a given zip code
    
    Args:
        zipcode: a 5-digit zip code given as a string
        
    Returns:
        Current temperature at zip code as a float
    """
    url = create_url(zip_code)
    
    with urllib.request.urlopen(url) as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
    # pretty_print(contents)
    d = json.loads(contents)
    
    print(d['main']['temp'])
    # return int(dist_meters / METERS_PER_MILE)

def get_field():
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    else:
        zip = sys.argv[1]
        get_temperature(zip)
