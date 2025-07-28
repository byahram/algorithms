N, M = map(int, input().split())
basket = [0] * N

for _ in range(0, M):
    i, j, k = map(int, input().split())
    for pos in range(i, j+1):
        basket[pos - 1] = k
        
for i in range(N):
    print(basket[i], end=" ")