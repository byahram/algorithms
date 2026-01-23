def solution(my_string):
    # answer = ''
    # for ch in my_string:
    #     if ch not in ["a", "e", "i", "o", "u"]:
    #         answer += ch
    # return answer

    return "".join([i for i in my_string if not(i in "aeiou")])