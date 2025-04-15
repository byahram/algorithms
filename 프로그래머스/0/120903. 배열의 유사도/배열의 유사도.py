def solution(s1, s2):
    # 1
    # answer = 0
    # for i in s1 :
    #     if i in s2 :
    #         answer += 1
    # return answer
    
    # 2
    # return len(set(s1) & set(s2))
    
    # 3
    return len(s1) + len(s2) - len(set(s1 + s2))