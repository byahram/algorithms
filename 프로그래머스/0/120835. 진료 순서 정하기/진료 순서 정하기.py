def solution(emergency):
    응급순서 = sorted(emergency, reverse=True)
    
    # 1.
    # return list(map(lambda x : 응급순서.index(x) + 1, emergency))
    
    # 2.
    return [응급순서.index(i) + 1 for i in emergency]