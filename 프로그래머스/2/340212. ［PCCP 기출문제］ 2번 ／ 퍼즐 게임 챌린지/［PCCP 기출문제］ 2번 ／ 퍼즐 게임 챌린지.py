def solution(diffs, times, limit):
    n = len(diffs)
    low, high = 1, max(diffs)
    
    while low < high:
        mid = (low + high) // 2
        total = 0
        
        for i in range(n):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= mid:
                total += time_cur
            else:
                mist = diff - mid
                time_prev = times[i-1]
                total += (time_cur + time_prev) * mist + time_cur
                
            if total > limit:
                break
                
        if total <= limit:
            high = mid
        else:
            low = mid + 1
            
    return low
                
        
    answer = 0
    return answer