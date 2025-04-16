def solution(age):
    char = 'abcdefghij'
    return ''.join(map(lambda x : char[int(x)], str(age)))