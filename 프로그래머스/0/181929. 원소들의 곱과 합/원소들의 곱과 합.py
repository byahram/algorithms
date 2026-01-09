def solution(num_list):
    mul = 1
    for n in num_list:
       mul *= n
    
    add = sum(num_list)
    return 1 if mul < (add ** 2) else 0