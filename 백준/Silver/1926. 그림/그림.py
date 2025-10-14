"""
1. 아이디어
    - 2중 for => 값 1 && 방문 X => BFS
    - BFS 돌면서 그림 개수 +1, 최댓값을 갱신

2. 시간복잡도
    - BFS: O(V+E)
    - V: 500 * 500
    - E: 4 * 500 * 500
    - V+E: 5 * 250000 = 100만 < 2억 >> 가능!

3. 자료구조
    - 그래프 전체 지도 : int[][]
    - 방문 : bool[][]
    - Queue(BFS)
"""

import sys
input = sys.stdin.readline

# n: 세로 길이(행), m: 가로 길이(열)
n, m = map(int, input().split())

# 그림이 그려진 전체 지도 (0: 빈칸, 1: 그림)
map = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부를 기록할 2차원 리스트
chk = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우 방향 정의 (델타 탐색)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# BFS 함수
def bfs(y, x):
    rs = 1                      # 현재 그림의 크기 (시작점 포함)
    q = [(y, x)]                # BFS용 큐 초기화 (리스트 사용)
    while q:
        ey, ex = q.pop()        # 큐의 마지막 원소를 꺼냄 (stack처럼 사용됨)
        for k in range(4):      # 4방향 탐색
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 좌표가 범위 안에 있고
            if 0 <= ny < n and 0 <= nx < m:
                # 방문하지 않았고 그림이 그려진 곳이면
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1              # 그림 크기 +1
                    chk[ny][nx] = True   # 방문 표시
                    q.append((ny, nx))   # 큐에 추가 (다음 탐색 대상)
    return rs  # 해당 그림의 넓이(크기)를 반환

cnt = 0     # 전체 그림 개수
maxv = 0    # 가장 큰 그림의 넓이

# 모든 좌표를 순회
for j in range(n):
    for i in range(m):
        # 방문하지 않은 그림(1)을 발견하면
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True     # 방문 표시
            cnt += 1             # 그림 개수 +1
            maxv = max(maxv, bfs(j, i))  # BFS로 크기 구하고 최댓값 갱신

# 결과 출력
print(cnt)   # 그림의 총 개수
print(maxv)  # 가장 넓은 그림의 넓이