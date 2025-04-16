from collections import deque

def solution(numbers, direction):
    # 1
    # if direction == 'right' :
    #     return [numbers[-1]] + numbers[:-1]
    # else :
    #     return numbers[1:] + [numbers[0]]
    
    # 2
    if direction == 'right' :
        numbers = deque(numbers)
        numbers.rotate(1) 
    else :
        numbers = deque(numbers)
        numbers.rotate(-1) 
    return list(numbers)