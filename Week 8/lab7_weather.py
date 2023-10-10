"""
Report the current weather from the web for a zip code

CS 150 Lab 7

Name: Finn Ellingwood
Section: B

Creativity: I made an extra optional argument in the entered command
which prints some extra weather info. I used some more of the API info to grab both
the name of the zip code's city and the current weather conditions
in the area in a single function returns a string that contains both
datum. The extra info will only be printed before the current temp
if the <True> argument is added after the zip code.
"""

import sys
import urllib.request
import json


BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?zip='

API = '64e3ee7a4b540e2c7591e68d94c9e664'

def create_url(zip_code):
    """
    Creates the open weather map url to access the API with given zipcode
    
    Args:
        zip_code: a 5-digit zip code given as a string
        
    Returns:
        The url to access the open weather API with correct key
    """
    url = str((BASE_URL + zip_code + ',us&APPID=' + API + '&units=imperial'))
    return url

def print_usage():
    """
    Prints the correct command usage when incorrect inline arguments given
    
    Args:
        none
        
    Returns:
        none
    """
    print('Usage: python3 lab7_weather.py <5-digit zip code> (optional arg for more weather info):<True>')

def get_temperature(zip_code):
    """
    Look up the current temperature at openweathermap for a given zip code
    
    Args:
        zipcode: a 5-digit zip code given as a string
        
    Returns:
        Current temperature at zip code as a float
    """
    url = create_url(zip_code)
    
    with urllib.request.urlopen(url) as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
    d = json.loads(contents)
    
    temp = ((d['main']['temp']))
    
    return temp

def get_conditions(zip_code):
    """
    Look up the current conditions cover for a given zip code
    
    Args:
        zipcode: a 5-digit zip code given as a string
        
    Returns:
        Current conditions at zip code as a string
    """
    with urllib.request.urlopen(BASE_URL + zip_code + ',us&APPID=' + API + '&units=imperial') as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
        d = json.loads(contents)
        
        name = str(d['name'])
        
        stringy = str(d['weather'])
    new_stringy = ''
        
    for i in range(len(stringy)-2):
        if i == 0 or i == 1:
            new_stringy += ''
        else:
            new_stringy += stringy[i]
            
    weather_list = new_stringy.split(",")
    weather_desc = str(weather_list[2:1:-3])
    weather_list = weather_desc.split(":")
    condition_unedited = str(weather_list[1])

    condition = ''

    for i in range(len(condition_unedited)-3):
        if i in range(2):
            condition += ''
        else:
            condition += condition_unedited[i]
            
    condition = (name+": \n"+ condition)
    return(condition)

if __name__ == "__main__":
    """
    Checks if zip was given correctly inline and then prints the location's temp
    and only runs when run through the run command, not when imported
    
    Args:
        zipcode: a 5-digit zip code given as a string
        
    Returns:
        nothing
    """
    if len(sys.argv) == 2:
        zip_code = sys.argv[1]
        temp = get_temperature(zip_code)
        print(temp)
    if len(sys.argv) == 3:
        while sys.argv[2] != 'True':
            print_usage()
            quit()
        zip_code = sys.argv[1]
        temp = get_temperature(zip_code)
        conds = get_conditions(zip_code)
        print("The current conditions around "+conds)
        print("And the current temperature in degrees F:")
        print(temp)
    elif len(sys.argv) != 3 and len(sys.argv) != 2:
        print_usage()