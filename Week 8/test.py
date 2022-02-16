import urllib.request
import json
with urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?zip=05753,us&APPID=64e3ee7a4b540e2c7591e68d94c9e664&units=imperial') as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
        d = json.loads(contents)
        
        cloudy = (d['weather'])
        
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
        
return(condition)