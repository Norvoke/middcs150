firstname = input("What is your first name ")
lastname = input("What is your last name ")
title = input("What is your title? ")
hailsfrom = input("From where do you hail? ")

fullname = [title, firstname, lastname]


i = 0

sentence = ''

while i < len(fullname):
    
    sentence += fullname[i] + ' '
    i += 1

sentence += 'of ' + hailsfrom 
print(sentence)

def scores(L):
    total = sum(L)
    print("Min: " min(L))
    print("Max: " max(L))
    print("Sum: " sum(L))
    print("Average: ", total / len(L))