def solution(n):
    count = 0
    num = 0
    
    while count < n:
        num += 1
        
        if num % 3 == 0 or '3' in str(num):
            continue            
        count += 1

    return num