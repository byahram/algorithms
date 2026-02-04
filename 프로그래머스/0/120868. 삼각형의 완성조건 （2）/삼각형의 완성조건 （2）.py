def solution(sides):
    a, b = sorted(sides)
    
    # 경우 1: b가 가장 긴 변 
    case1 = max(0, b - (b - a + 1) + 1)
    
    # 경우 2: x가 가장 긴 변 
    case2 = max(0, (a + b - 1) - (b + 1) + 1)
    
    return case1 + case2