"""
Write weather information over time to a file

CS 150 Lab 7

Name: Finn Ellingwood
"""
import lab7_weather as lab7
import datetime
import sys
import os.path

def print_usage():
    """
    Prints the correct command usage when incorrect inline arguments given
    
    Args:
        none
        
    Returns:
        none
    """
    print('usage: python3 lab7_aggregator.py <file> <zip_code>')
   
def get_hour():
    """
    Returns the current hour of the day using the datetime module
    """
    
    now = datetime.datetime.now()
    return str(now.hour)
   
def get_date():
    """
    Returns the current date using the datetime module
    """
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

def check_file(file_name):
    """
    Checks if the file_name exists and if the current hour/date was recorded
    
    Returns:
        True: if weather was already recorded
        
        False: is weather was not yet recorded
    """
    date = str(get_date())
    hour = str(get_hour())
    entry = str(date+','+hour)
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                if line.startswith(entry):
                    return True
                else:
                    return False
    else:
        return False
    
def create_entry(zip_code):
    """
    Calls on the weather module to grab the temp from the API and
    creates the entry for the file given the zipcode.
    
    Args:
        zip_code: 5-digit zipcode of desired location
    
    Returns:
        A string of comma seperated values with the format:
            <DATE,HOUR,TEMP>
    """
    temp = str(lab7.get_temperature(zip_code))
    date = str(get_date())
    hour = str(get_hour())
    
    entry = str(date+','+hour+','+temp)
    
    return entry

def write_entry(zip_code, file_name):
    """
    Creates file if it doesn't exist, then writes to file the entry created
    by the create_entry module
    
    Args:
        zip_code: 5-digit zipcode of desired location
        
        file_name: desired file name to be appended to or created
    
    Returns:
        nothing
        
    """
    if check_file(file_name):
        return
    else:
        with open(file_name, "a") as file:
            file.write(create_entry(zip_code))
            file.write("\n")
            file.close()
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
    else:
        file_name = sys.argv[1]
        zip_code = sys.argv[2]
        write_entry(zip_code, file_name)
    