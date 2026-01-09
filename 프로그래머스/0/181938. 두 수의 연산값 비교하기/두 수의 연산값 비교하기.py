def solution(a, b):
    formula1 = int(str(a) + str(b))
    formula2 = 2 * a * b
    return formula1 if formula1 >= formula2 else formula2