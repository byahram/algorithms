def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch not in ["a", "e", "i", "o", "u"]:
            answer += ch
    return answer