"""
Write weather information over time to a file

CS 150 Lab 7

Name: Finn Ellingwood
"""
import lab7_weather as lab7
import datetime
import sys

def print_usage():
    print('usage: python3 lab7_aggregator.py <file> <zip_code>')
   
def get_hour():
    """
    Return the current hour of the day using the datetime module
    """
    
    now = datetime.datetime.now()
    return str(now.hour)
   
def get_date():
    """
    Return the current date using the datetime module
    """
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

def check_file():
    #if file does not exist
        #True
    #if line.startswish(date_time)
        #False
    pass
    
def write_entry(entry, filename):
    with open(filename, 'a') as file:
        file.write(entry)
    pass
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
    else:
        file_name = sys.argv[1]
        zip = sys.argv[2]
        temp = lab7.get_temperature(zip)
        
    