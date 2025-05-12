def solution(array, n):
    # 1.
    # array = sorted(array)
    # diff = float("inf")
    # nearest = 0
    # for i in array :
    #     if abs(n - i) < diff :
    #         diff = n - i
    #         nearest = i
    # return nearest
    
    # 2. 
    return sorted(array, key = lambda x : (abs(x - n), x - n))[0]