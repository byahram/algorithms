from math import factorial

def solution(n):
    # 1.
    # factorial = 1
    # i = 1
    # while factorial <= n :
    #     i += 1
    #     factorial *= i
    # return i - 1
    
    # 2. 
    i = 1
    while factorial(i) <= n :
        i += 1
    return i - 1
