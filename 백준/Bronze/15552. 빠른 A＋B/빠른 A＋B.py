import sys

T = int(input())

for _ in range(1, T + 1):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
    