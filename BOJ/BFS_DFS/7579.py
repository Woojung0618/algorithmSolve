import sys
from collections import deque
m, n, k = map(int, input().split())
graph = []
time = []

for j in range(k):
    row, row0 = [], []
    for i in range(n):
        row.append(list(map(int, sys.stdin.readline().split())))
        row0.append([0 for _ in range(m)])
    graph.append(row)
    time.append(row0)

# 모두 익은 경우에는 0 출력
iszero = False
for i in range(k):
    for j in range(n):
        if 0 in graph[i][j]:
            iszero = True
            break
if iszero == False:
    print(0)
    exit(0)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    queue = deque()
    for i in range(k):
        for j in range(n):
            for u in range(m):
                if graph[i][j][u] == 1:
                    queue.append((i, j, u))
    while queue:
        x, y, z = queue.popleft()
        for r in range(6):
            nx = x + dx[r]
            ny = y + dy[r]
            nz = z + dz[r]
            if nx < 0 or ny < 0 or nz < 0 or nx >= k or ny >= n or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1
                time[nx][ny][nz] = time[x][y][z] + 1
                queue.append((nx, ny, nz))
bfs()
for i in range(k):
    for j in range(n):
        if 0 in graph[i][j]:
            print(-1)
            exit(0)
answer = 0
for i in range(k):
    for j in range(n):
        for u in range(m):
            if answer < time[i][j][u]:
                answer = time[i][j][u]
print(answer)