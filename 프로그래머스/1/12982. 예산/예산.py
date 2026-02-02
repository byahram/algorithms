def solution(d, budget):
    answer = 0
    d.sort()
    for w in d:
        budget -= w
        if budget >= 0:
            answer += 1 
    return answer