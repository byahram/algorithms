def solution(order):
    # 1
    # answer = 0
    # order = str(order)
    # answer += order.count('3')
    # answer += order.count('6')
    # answer += order.count('9')
    
    # 2. map
    # order = str(order)
    # return sum(map(lambda x : order.count(x), '369'))
    
    # 3. filter
    # order = str(order)
    # return len(list(filter(lambda x: x in '369', order)))
    
    # 4. 정규표현식
    import re
    
    order = str(order)
    return len(re.findall('[369]', order))