import sys
from collections import deque
import copy
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

# for문 돌면서 3개 싹다 세우고, O(64*63*62) = O(20만)
# 안전공간 체크 - bfs

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(cnt + 1)
                maps[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    graph = copy.deepcopy(maps)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
    cnt = 0
    global answer
    for i in range(n):
        cnt += graph[i].count(0)
    answer = max(answer, cnt)

answer = 0
wall(0)
print(answer)