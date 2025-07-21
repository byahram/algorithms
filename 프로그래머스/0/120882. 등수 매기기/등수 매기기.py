def solution(score):
    answer = sorted([sum(i) for i in score], reverse = True)
    return [answer.index(sum(j)) + 1 for j in score]