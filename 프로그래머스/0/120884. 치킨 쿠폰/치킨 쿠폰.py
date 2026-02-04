def solution(chicken):
    coupons = chicken
    service = 0
    
    while coupons >= 10:
        free = coupons // 10           # 받을 수 있는 서비스 치킨
        service += free                # 누적
        coupons = coupons % 10 + free  # 남은 쿠폰 + 새 쿠폰
    
    return service