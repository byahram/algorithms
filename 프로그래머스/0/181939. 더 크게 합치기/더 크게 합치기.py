def solution(a, b):
    ab = int(f"{str(a)}{str(b)}")
    ba = int(f"{str(b)}{str(a)}")
    return ab if ab == ba else max(ab, ba)