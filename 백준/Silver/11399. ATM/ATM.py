import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

# 정렬
A.sort()
S[0] = A[0]

# 합 배열 
for i in range(1, N):
    S[i] = S[i-1] + A[i]
    
print(sum(S))