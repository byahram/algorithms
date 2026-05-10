def solution(clothes):
    # 1. 의상 종류별로 개수 세기
    closet = {}
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1
    
    # 2. (종류별 개수 + 1)을 모두 곱하기
    answer = 1
    for count in closet.values():
        answer *= (count + 1)
        
    # 3. 최소 하나는 입어야 하므로 '전체 안 입음' 경우인 1을 뺌
    return answer - 1