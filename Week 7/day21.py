dates_times_temps = ['4-8-2022,8,38.02', '4-8-2022,9,39.05', '4-8-2022,10,41.11']
    
s = '4-8-2022,11,41.11'

def existing_entry(data, s):
    """
    Determins if s already appears in data
    """
    for element in data:
        print(element)
        if element.startswith(s):
            return True
    
    return False
            