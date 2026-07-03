def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char) # 여는 괄호는 push
        else:
            if not stack: # 닫는 괄호인데 스택이 비어있으면 실패
                return False
            stack.pop() # 짝을 맞췄으므로 pop

    # 모든 순회 후 스택이 깨끗하게 비어있어야 성공
    return len(stack) == 0