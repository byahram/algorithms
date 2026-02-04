def solution(board):
    n = len(board)
    danger = [[0] * n for _ in range(n)]
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 0),  (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = 1
    
    safe = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe += 1
    return safe