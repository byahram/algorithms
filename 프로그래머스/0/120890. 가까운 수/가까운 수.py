def solution(array, n):
    array = sorted(array)
    diff = float("inf")
    nearest = 0
    for i in array :
        if abs(n - i) < diff :
            diff = n - i
            nearest = i
    return nearest