def solution(n, control):
    answer = 0
    dic = {"w": 1, "s": -1, "d": 10, "a": -10}
    
    for str in control:
        n += dic[str]
    return n