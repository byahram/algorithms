def solution(num_list):
    answer = [0, 0]
    for num in num_list :
        # 1
        # if num % 2 == 0 :
        #     answer[0] += 1
        # else :
        #     answer[1] += 1
        
        # 2
        answer[num % 2] += 1
    return answer