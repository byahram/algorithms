year = int(input())

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(int("1"))
else:
    print(int("0"))