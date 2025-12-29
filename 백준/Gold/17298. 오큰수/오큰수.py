import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
myStack = [] 

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        idx = myStack.pop()
        answer[idx] = A[i]
        
    myStack.append(i)

print(*answer)