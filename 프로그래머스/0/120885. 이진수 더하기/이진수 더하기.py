def solution(bin1, bin2):
    num1, num2 = int(bin1, 2), int(bin2, 2)
    return bin(num1 + num2)[2:]