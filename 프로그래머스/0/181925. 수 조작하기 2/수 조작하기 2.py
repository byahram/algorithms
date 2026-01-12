def solution(numLog):
    answer = ""
    dic = {1: "w", -1: "s", 10: "d", -10: "a"}
    
    for i, num in enumerate(numLog):
        if i != 0:
            str = dic[numLog[i] - numLog[i-1]]
            answer += str
        
    return answer