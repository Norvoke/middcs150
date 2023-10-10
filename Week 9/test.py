def mystery(a_list):
     a_list = a_list[:]
     a_list.sort()
     a_list[1].append(2)
     return a_list[0][0]
    
a = [[3], [7], [2], [9], [1]]
result = mystery(a)