def solution(prices):
    # 각 시점에서 가격이 떨어지지 않은 시간을 저장
    answer = [0] * len(prices)

    # 아직 가격이 떨어지지 않은 시점의 인덱스를 저장
    stack = []

    for i in range(len(prices)):

        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    while stack:
        j = stack.pop()

        answer[j] = len(prices) - 1 - j

    return answer