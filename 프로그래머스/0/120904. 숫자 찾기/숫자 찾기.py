def solution(num, k):
    li = list(str(num))
    return li.index(str(k)) + 1 if str(k) in li else -1