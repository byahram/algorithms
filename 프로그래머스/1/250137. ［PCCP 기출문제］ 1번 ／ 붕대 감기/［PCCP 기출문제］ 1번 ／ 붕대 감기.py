def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    last_time = attacks[-1][0]
    
    attack_id= 0
    combo = 0
    
    
    for time in range(1, last_time + 1):
        # 공격 시간인지 먼저 확인
        if attack_id <= len(attacks) and attacks[attack_id][0] == time:
            health -= attacks[attack_id][1]
            attack_id += 1
            combo = 0  # 공격 받으면 연속 성공 초기화
            
            if health <= 0:
                return -1
        else:
            # 공격이 아니라면 회복
            health += x
            combo += 1
            
            # t초 연속 성공 시 추가 회복
            if combo == t:
                health += y
                combo = 0
                
            # 최대 체력 제한
            if health > max_health:
                health = max_health
    
    return health