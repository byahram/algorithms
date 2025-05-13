def solution(emergency):
    응급순서 = sorted(emergency, reverse=True)
    return list(map(lambda x : 응급순서.index(x) + 1, emergency))