def solution(n, control):
    answer = n
    dic = {"w": 1, "s": -1, "d": 10, "a": -10}
    
    for str in control:
        answer += dic[str]
    return answer