from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행, 열
    queue = deque([(0, 0)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]