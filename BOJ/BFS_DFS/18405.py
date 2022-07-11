import sys
from collections import deque
n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    cnt = 0
    q = deque(virus)
    # q = deque(sorted(q, key=lambda x: x[2]))  # -> 시간 초과
    # q = deque(sorted(list(q), key=lambda x: x[2]))  # -> 매번 정렬할 필요 X
    while q:
        if cnt == s:
            return
        for _ in range(len(q)):
            x, y, z = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = z
                    q.append((nx, ny, graph[nx][ny]))
        cnt += 1
        # print(graph)

virus = []
for i in range(n):
    for j in range(n):
        virus.append((i, j, graph[i][j]))
virus.sort(key=lambda x: x[2]) # 세번째 값인 z로 정렬

bfs()

if graph[x-1][y-1] == 0:
    print(0)
else:
    print(graph[x-1][y-1])
