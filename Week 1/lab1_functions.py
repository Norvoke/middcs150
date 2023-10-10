"""
CSCI 150 Lab 1

Name: Finn Ellingwood
Section (A or B): B

Creativity: The function european_minimum_wage uses the average minimum
wage across the EU to determine how much one would get paid in USD
for working a certain amound of hours.

"""
def euros_to_dollars(euros):
    """
    Args:
        euros: an amount of euros to be converted to dollars
        
    Returns:
        The value of the euros converted to dollars at the exchange
        rate of 1.21:1
    """
    return euros * 1.21

def welcome():
    """
    prints "welcome" in Spanish.
    """
    return ('Bienvenidos')

def kilometers_to_miles(kilometers):
    """
    Args:
        kilometers: An amount of kilometers to be converted to miles
    
    Returns
        The value of the kilometers converted to miles at the
        rate if 1:.6214
    """
    return kilometers * 0.6214

def celsius_to_fahrenheit(celsius):
    """
    Args:
        celsius: a temperature in degrees celsius to be converted to fahrenheit
        
    Returns:
        The temperature in celcius converted to degrees fahrenheit using the
        conversion (celsius * (9/5)) + 32 = fahrenheit.
    """
    return (celsius * (9/5)) + 32

def mpg_from_metric(kilometers, liters):
    """
    Args:
        kilometers: A number of kilometers to be divided by liters to
        be converted to miles per gallon
        liters: A number of liters to divide the kilometers to be
        converted to miles per gallon
        
    Returns:
        The kilometers per liter converted to miles per gallon at the rate
        of 1 kilometers per .6214 miles and 1 liter per .2642
    """
    return (kilometers * 0.6214)/(liters * 0.2642)
# ---------------------- 
# Section 2: Functions that print
# ----------------------

def four_fours():
    """
    Args: None.
    
    Returns:
        The numbers 0-9 as integers using exactly four 4s.
    """
    print(4+4-4-4, "is 4+4-4-4")  # 0
    print(4//4*4//4, "is 4/4*4/4")  # 1
    print(4//4+4//4, "is 4/4+4/4")  # 2
    print((4+4+4)//4, "is (4+4+4)/4")  # 3
    print(4%4%4+4, "is 4%4%4+4")  # 4
    print((4*4+4)//4, "is 4*4+4)/4")  # 5
    print((4+4)//4+4, "is (4+4)/4+4")  # 6
    print(4-(4//4)+4, "is 4-(4/4)+4")  # 7
    print(4+4+4-4, "is 4+4+4-4")  # 8
    print(4+4+4//4, "is 4+4+4/4")  # 9

def convert_from_seconds(seconds):     
    """
    Print number of days, hours, minutes, and seconds in a given number of seconds.
    
    Args:
        seconds: non-negative integer representing number of seconds
    
    Returns:
        None
    """
    days = seconds // (24 * 60 * 60) # Number of days
    leftover_seconds = seconds % (24 * 60 * 60) # The leftover seconds
    hours = leftover_seconds // (60 * 60) # Number of hours
    leftover_seconds = seconds % (60 * 60) # The leftover seconds for minutes
    minutes = leftover_seconds // (60) # Number of minutes
    leftover_seconds = seconds % (60) # The leftover seconds for seconds
    print(days, "days")
    print(hours, "hours")
    print(minutes, "minutes")
    print(leftover_seconds, "seconds")
    
def european_minimum_wage(hours):
    """
    Calculates the amount of money in dollars you would get paid for working
    a certain amount of hours for the average minumum wage in Europe (EU).
    
    Args:
        hours: Number of hours worked to be multiplies by the average minimum wage
        
    Returns:
        The pay in dollars one would recieve for working minimum wage at a rate of €10.45
        per hour
    """
    return euros_to_dollars(10.45 * hours)
    


