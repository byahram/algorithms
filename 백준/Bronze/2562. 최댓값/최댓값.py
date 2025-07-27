import sys

n_list = []

for _ in range(0, 9):
    N = int(sys.stdin.readline())
    n_list.append(N)
    
print(max(n_list))
print(n_list.index(max(n_list)) + 1)