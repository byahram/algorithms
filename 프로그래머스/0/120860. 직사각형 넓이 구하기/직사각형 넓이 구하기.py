def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    y = max(y) - min(y)
    
    return w * y