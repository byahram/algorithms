def solution(t, p):
    answer = 0
    for i in range(0, len(t)):
        if len(t[i:i+len(p)]) == len(p):
            if int(t[i:i+len(p)]) <= int(p):
                answer += 1 
    return answer