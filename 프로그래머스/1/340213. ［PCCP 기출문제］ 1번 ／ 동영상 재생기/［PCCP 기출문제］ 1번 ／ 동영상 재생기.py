def solution(video_len, pos, op_start, op_end, commands):
    vm, vs = map(int, video_len.split(":"))
    pm, ps = map(int, pos.split(":"))
    sm, ss = map(int, op_start.split(":"))
    em, es = map(int, op_end.split(":"))
    
    V = vm * 60 + vs
    P = pm * 60 + ps
    S = sm * 60 + ss
    E = em * 60 + es
    
    if S <= P <= E:
        P = E
        
    for cmd in commands:
        if cmd == "prev":
            P -= 10
            if P < 0:
                P = 0
        elif cmd == "next":
            P += 10
            if P > V:
                P = V
                
        if S <= P <= E:
            P = E
            
    mm = P // 60
    ss = P % 60
        
    return f"{mm:02d}:{ss:02d}"