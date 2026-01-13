from collections import Counter

def solution(array):
    counter = Counter(array)
    max_freq = max(counter.values())
    list = [k for k, v in counter.items() if v == max_freq]
    
    return -1 if len(list) > 1 else list[0]