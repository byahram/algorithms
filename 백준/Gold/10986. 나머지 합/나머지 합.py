import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 1. 합 배열 만들기
S = [0] * N
C = [0] * M
answer = 0

S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]
	
# 2. 합 배열의 나머지 계산 및 개수 카운팅
for i in range(N):
    remainder = S[i] % M
    
    # 1) 0번 인덱스부터 i까지의 합 자체가 나누어 떨어지는 경우
    if remainder == 0:
        answer += 1
    
    # 2) 나머지가 같은 인덱스의 개수 카운팅
    C[remainder] += 1
	
# 3. 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더하기
for i in range(M):
    if C[i] > 1:
        # nC2 = n * (n-1) / 2
        answer += (C[i] * (C[i]-1) // 2)

print(answer)