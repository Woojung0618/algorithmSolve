import sys
from collections import deque
n, L, R = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    sum_value = graph[a][b]
    count = 1
    opens = [(a, b)]
    queue = deque()
    queue.append((a, b))
    visit[a][b] = 1
    while queue:
        x, y = queue.popleft()
        # print(x,y)
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] == 0 and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                sum_value += graph[nx][ny]
                count += 1
                opens.append((nx, ny))
                queue.append((nx, ny))
                visit[nx][ny] = 1
                    
    value = sum_value // count
    for i, j in opens:
        graph[i][j] = value
    return count


answer = 0
while True:
    visit = [[0] * n for _ in range(n)]
    stop = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                temp = bfs(i, j)
                if temp > 1:
                    stop = True
    if stop == False:
        break
    answer += 1
    
print(answer)

