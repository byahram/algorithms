def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, n + 1):
            if i % j == 0:
                divisor += 1
                if divisor >= 3:
                    cnt += 1
                    break
    return cnt