import sys
input = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())

# 2. 원본 배열 A
A = [[0] * (N+1)]
for _ in range(N):
    A.append([0] + list(map(int, input().split())))

# 3. 합 배열 D 만들기
D = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 4. 질의 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)