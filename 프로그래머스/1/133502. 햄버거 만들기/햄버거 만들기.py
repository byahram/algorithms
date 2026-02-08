def solution(ingredient):
    count = 0
    stack = []
    
    for ing in ingredient:
        stack.append(ing)
        
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            count += 1
            
    return count