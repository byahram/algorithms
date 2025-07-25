import sys

while 1:
    A, B = map(int, sys.stdin.readline().split())
    
    if A == 0 and B == 0:
        break
    else:
        print(A + B)