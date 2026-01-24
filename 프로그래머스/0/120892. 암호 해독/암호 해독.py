def solution(cipher, code):
    # 1.
    # answer = ''
    # for ch in range(code-1, len(cipher), code):
    #     answer += cipher[ch]
    # return answer
    
    # 2.
    return "".join(cipher[ch] for ch in range(code-1, len(cipher), code))