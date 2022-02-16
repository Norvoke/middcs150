def iterable_to_string(iterable):
    l = ''
    if type(iterable) == str:
        for element in range(0, len(iterable)):
            l += str(iterable[element]+' ')
        return l
    elif type(iterable) == list:
        for element in range(0, len(iterable)):
            l += str(str(iterable[element])+' ')
        return l
    elif type(iterable) == set:
        for item in iterable:
            l +=(str(item)+' ')
        return l