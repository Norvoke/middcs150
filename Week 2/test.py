def phase(temp):
    if 0 < temp < 100:
        return "liquid"
    elif temp <= 0:
        return "solid"
    else:
        return "vapor"