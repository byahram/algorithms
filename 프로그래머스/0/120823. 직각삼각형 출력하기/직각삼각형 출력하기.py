n = int(input())
for i in range(1, n+1):
    print("*" * i)
    
# *를 붙여서 제너레이터 안의 내용을 꺼내줌.
# print(*("*" * i for i in range(1, n+1)), sep='\n')