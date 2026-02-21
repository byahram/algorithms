# from collections import Counter

def solution(participant, completion):
    # 3. hash dictionary 사용
    hash_dict = {}

    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1

    for c in completion:
        hash_dict[c] -= 1

    for k in hash_dict:
        if hash_dict[k] > 0:
            return k
    
    # 2. 
    # participant.sort()
    # completion.sort()
    # 
    # for p, c in zip(participant, completion):
    #     if p != c:
    #         return p
    # 
    # return participant[-1]
    
    # 1. Counter 사용
    # diff = Counter(participant) - Counter(completion)
    # return next(iter(diff))