def count_lines(filename):

    linenum = 0
    line_list = []

    with open(filename, "r") as file:
        file_string = file.read()
        line_list = file_string.split("\n")
    
        for i in line_list:
            if i:
                linenum += 1
    return linenum

def odds(numset):
    oddset = set()
    
    for element in numset:
        if (element % 2) == 1:
            oddset.add(element)
    return oddset
        