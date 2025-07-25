X = int(input())
N = int(input())
sum = 0

while N > 0:
    a, b = map(int, input().split())
    sum += (a * b)
    N -= 1
    
print("Yes" if sum == X else "No")