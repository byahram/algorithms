def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, z = q.split()
        x, y, z = int(x), int(y), int(z)
        
        val = x + y if op == "+" else x - y
        answer.append("O" if val == z else "X")
    return answer