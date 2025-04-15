import numpy as np 

def solution(numbers):
    # 1
    # answer = []
    # for i in numbers :
    #     answer.append(i * 2)
    # return answer
    
    # 2
    # return list(map(lambda x:x*2, numbers))
    
    # 3
    numbers = np.array(numbers)
    return (numbers * 2).tolist()