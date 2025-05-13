import re

def solution(my_str, n):
    # 1.
    # p = re.compile(f'.{{1,{n}}}')
    # return p.findall(my_str)
    
    # 2.
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]