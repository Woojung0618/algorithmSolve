import sys
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def bfs(s):
    queue = deque([s])
    visit[s] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = 1
    return

answer = 0

for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        answer += 1
print(answer)
