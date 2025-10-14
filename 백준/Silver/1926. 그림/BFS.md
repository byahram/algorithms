# **BFS (Breadth-First Search, 너비 우선 탐색)**

## 1. 개념

- **그래프 탐색(Traversal)**  
  → 여러 개의 노드(Vertex)가 **간선(Edge)** 로 연결된 구조에서  
  **연속적으로 이어진 모든 노드들을 탐색(방문)** 하는 방법 중 하나.

- **그래프(Graph)** =  
  **Vertex(정점, 어떤 것)** + **Edge(간선, 이어지는 관계)**

- **그래프 탐색 방식**

  | 구분    | 이름                 | 탐색 순서                     | 사용 구조                   |
  | ------- | -------------------- | ----------------------------- | --------------------------- |
  | **BFS** | Breadth-First Search | 가까운 노드부터 **넓게 탐색** | **Queue(큐)**               |
  | **DFS** | Depth-First Search   | 한 방향으로 **깊게 탐색**     | **Stack(스택) or 재귀함수** |

## 2. BFS 아이디어 (동작 원리)

1. **시작점**을 큐에 넣고, 방문 표시
2. 큐에서 **가장 먼저 들어온 노드**를 꺼냄 (FIFO)
3. 그 노드와 **연결된 인접 노드** 중
   - 아직 방문하지 않은 노드를
   - 큐에 추가하고 방문 표시
4. 큐가 빌 때까지 반복

**가까운 곳부터 차례로 퍼져나가는 구조**  
(예: 파도 확산, 최단거리 탐색, 영역 탐색 등)

## 3. 시간 복잡도

> BFS의 시간 복잡도 = **O(V + E)**
>
> - `V`: 정점(Vertex)의 개수
> - `E`: 간선(Edge)의 개수

```md
예시

- 500 × 500 격자 → 정점 250,000개
- 각 정점당 최대 4개의 간선 → 약 1,000,000회 연산
  - **충분히 가능 (2억 미만이면 안전)**
```

## 4. 필요한 자료구조

| 역할      | 자료형                | 설명                               |
| --------- | --------------------- | ---------------------------------- |
| 그래프    | `list[list[int]]`     | 탐색 대상 (2D grid, 인접리스트 등) |
| 방문체크  | `list[list[bool]]`    | 방문 여부 기록 (중복 방지)         |
| 큐(Queue) | `collections.deque()` | BFS 탐색 순서를 관리               |

## 5. BFS 기본 코드 템플릿

### 1) 구역 탐색용 BFS (영역 개수 / 크기 세기)

- “서로 연결된 구역의 개수나 크기를 구할 때”
- **예시:** 그림 개수, 섬의 개수, 단지번호붙이기 등
- 특징
  - BFS 1회 = 한 구역 전체 탐색
  - 전체 탐색 시 2중 for문 + 방문체크
  - area 로 넓이 계산

```python
from collections import deque

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    area = 1                     # 구역 크기 (시작점 포함)

    while q:
        cy, cx = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    area += 1
    return area
```

### 2) 거리 계산용 BFS (단계별 확산 / 최소 이동 횟수)

- “시작점에서 각 지점까지의 거리(이동 횟수)를 구할 때”
- 예시: 미로 탐색, 토마토, 전염, 불 확산 등
- 특징
  - dist 배열을 따로 만들어 거리 저장
  - BFS 특성상 처음 도달한 값이 최단 거리
  - dist = -1 로 초기화 후 방문 시 dist + 1

```py
from collections import deque

def bfs(sy, sx):
    q = deque([(sy, sx)])
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
```

### 3) 최단 경로 복원용 BFS (경로까지 추적)

- “최단 거리뿐 아니라 경로 자체를 출력해야 할 때”
- 예시: 숨바꼭질, 미로에서 탈출 경로 출력 등
- 특징
  - 거리(dist)와 부모 노드(parent) 를 함께 기록
  - BFS 종료 후 parent 배열을 역추적하여 경로 복원

```py
from collections import deque

def bfs(start):
    q = deque([start])
    dist[start] = 0
    parent[start] = -1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                parent[nxt] = cur
                q.append(nxt)

# 경로 복원
def reconstruct_path(end):
    path = []
    while end != -1:
        path.append(end)
        end = parent[end]
    return path[::-1]   # 역순으로 뒤집기
```

### 4) 3D BFS (3차원 공간 탐색)

- “입체적 구조나 3차원 격자(예: 토마토, 빙하, 건물 등)”
- 예시: 3D 토마토 익히기, 3층 미로 등
- 특징
  - 6방향 탐색 (상하좌우위아래)
  - 차원 수만 늘어날 뿐 기본 BFS 구조 동일
  - graph[z][y][x] 로 접근

```py
from collections import deque

def bfs():
    q = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    q.append((z, y, x))

    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))
```

## 6. BFS의 대표 활용 예시

| 유형          | 목적                    | 대표 예시       | 주요 변수         | 반환값         |
| ------------- | ----------------------- | --------------- | ----------------- | -------------- |
| **구역 탐색** | 연결된 영역 개수 / 크기 | 그림, 섬, 단지  | `visited`, `area` | 면적(크기)     |
| **거리 계산** | 최소 이동 횟수          | 미로, 토마토    | `dist`            | 거리값         |
| **경로 복원** | 실제 이동 경로 출력     | 숨바꼭질, 탈출  | `parent`          | 경로 리스트    |
| **3D BFS**    | 입체적 확산 탐색        | 3D 토마토, 건물 | `z, y, x`         | 거리 또는 단계 |

## 정리 요약 (암기 포인트)

> **BFS = Queue + 방문체크 + 반복문**
>
> 🔹 가까운 곳부터 탐색
> 🔹 FIFO 구조 (선입선출)
> 🔹 시간복잡도 O(V+E)
> 🔹 전형적 사용 예: **그림 개수, 최단거리, 감염 퍼짐**
