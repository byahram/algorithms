def solution(rsp):
    # 1
    # answer = ''
    # for i in rsp :
    #     if i == '0' :
    #         answer += '5'
    #     elif i == '2' :
    #         answer += '0'
    #     elif i == '5' :
    #         answer += '2'
    # return answer
    
    # 2
    d = {'0':'5', '2':'0', '5':'2'}
    return ''.join([d[i] for i in rsp])