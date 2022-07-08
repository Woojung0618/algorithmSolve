import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return 
    
T = int(input())
for _ in range(T):
    answer = 0
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)