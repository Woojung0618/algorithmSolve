import sys
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
parent = [0] * (n+1)
for _ in range(n-1):
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
                parent[i] = x
    return parent
answer = bfs(1)
# print(answer)
for a in range(2, len(answer)):
    print(answer[a])