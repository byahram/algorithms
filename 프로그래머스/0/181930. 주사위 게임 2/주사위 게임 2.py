def solution(a, b, c):
    chk = len(set([a, b, c]))
    
    if chk == 3:
        return a + b + c
    elif chk == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)