def solution(s):
    answer = 0
    x = ""
    x_cnt, n_cnt = 0, 0    
    
    for ch in s:

        if x_cnt == 0:
            x = ch
            x_cnt += 1
            answer += 1
            continue
            
        if ch == x:
            x_cnt += 1
        else:
            n_cnt += 1

        if x_cnt == n_cnt:
            x_cnt = 0
            n_cnt = 0
        
    return answer