def solution(num_list):
    mul = 1
    add = 0
    
    for n in num_list:
        mul *= n
        add += n
    
    return 1 if mul < (add ** 2) else 0