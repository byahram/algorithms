def solution(n):
    answer = [n]
    while n > 1:
        n = (n // 2) if n % 2 == 0 else (3 * n + 1)
        print(n)
        answer.append(n)
        print(answer)
    
    return answer