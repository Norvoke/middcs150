"""
CS 150 Examples
"""




def my_function(a, b):
    a += b
    return True

# def mystery1(a):
#     a.sort()
#     a[2].append(10)
#     return a
# 
# b = [[3],[1],[2]]
# c = mystery1(b)
# print('mystery1:')
# print('b:', b)
# print('c:', c)
# 
# def my_function(a, b):
#     a += b
#     return True

def mystery2(a):
    a = sorted(a)
    a[2].append(10)
    return a

b = [[3],[1],[2]]
c = mystery2(b)
print('mystery2:')
print('b:', b)
print('c:', c)