from collections import deque
import sys

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    if len(graph[i]) > 1:
        graph[i].sort()
# print(graph)

check_b = [0] * (n+1)
check_d = [0] * (n+1)

def bfs(x):
    queue = deque([x])
    check_b[x] = 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if check_b[i] == 0:
                queue.append(i)
                check_b[i] = 1
                



def dfs(x):
    check_d[x] = 1
    print(x, end=' ')
    for i in graph[x]:
        if check_d[i] == 0:
            dfs(i)
dfs(v)
print()
bfs(v)