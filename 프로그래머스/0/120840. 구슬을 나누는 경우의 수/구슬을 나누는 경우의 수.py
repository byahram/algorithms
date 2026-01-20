import math

def solution(balls, share):
    # 1. 파이썬 내장 math.comb
    return math.comb(balls, share)

    # 2. 팩토리얼로 직접 계산
    # return (math.factorial(balls)) // (math.factorial(balls-share) * math.factorial(share))