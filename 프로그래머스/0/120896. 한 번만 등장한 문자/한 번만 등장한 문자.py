from collections import Counter

def solution(s):
    # 1.
    # return "".join(sorted([c for c in s if s.count(c) == 1]))
    
    # 2.
    string = []
    for i, j in Counter(s).items() :
        if j == 1 :
            string.append(i)
    return ''.join(sorted(string))