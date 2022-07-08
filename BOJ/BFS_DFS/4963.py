import sys
from collections import deque 

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        exit()
    graph = []
    answer = 0
    for _ in range(h):
        row = list(map(int, sys.stdin.readline().split()))
        graph.append(row)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)