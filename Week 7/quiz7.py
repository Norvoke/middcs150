import sys
print(__name__)
print(len(sys.argv))
if __name__ == '__main__':
    a = sys.argv[ 1 ]
    b = sys.argv[ 2 ]
    print('run as main', a * int(b))
else:
    print('imported')