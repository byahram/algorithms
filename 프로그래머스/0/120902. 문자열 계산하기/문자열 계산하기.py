def solution(my_string):
    li = my_string.split()
    answer = int(li[0])
    
    for i in range(1, len(li), 2):
        operator = li[i]
        number = int(li[i + 1])
        
        if operator == "+":
            answer += number
        elif operator == "-":
            answer -= number
    return answer