def solution(my_string):
    return sum(int(ch) for ch in my_string if ch.isdigit())