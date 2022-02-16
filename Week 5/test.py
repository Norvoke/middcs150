def middle(list):
    if len(list) % 2 == 1:
        midd = int(len(list) / 2 - 0.5)
        return list[midd]
    else:
        midd = int(len(list) / 2)
        midd = (list[midd] + list[midd - 1]) / 2
        return midd
    
def mode(data):
    
    """
    Attempts to return the mode of the list data
    
    Args:
        data: List of "sortable" data items
    """
    
    mode = (max(set(data), key = data.count))
    
    return mode

