import sys

N, X = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
print(*[i for i in n_list if i < X])

# for i in n_list:
#     if i < X:
#         print(i, end=" ")