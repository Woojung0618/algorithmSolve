# 2가지 방식으로 풀이 (백준 사이트 제출 참고)
import sys
from collections import deque
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
time = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                time[nx][ny] = time[x][y] + 1
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return

bfs()
for i in range(n):
    if 0 in graph[i]:
        print(-1)
        exit()

print(max(map(max, time)))  ### 2차원 배열에서는 map 이용해서 최댓값 구하기