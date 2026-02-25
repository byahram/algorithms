def solution(arr):
    answer = []
    for i, a in enumerate(arr):
        if len(answer) == 0 or a != answer[-1]:
            answer.append(a)
    return answer