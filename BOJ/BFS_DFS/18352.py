import sys
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [0] * (n+1)
distance = [0] * (n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
# print(graph)

from collections import deque
def bfs(x):
    answer = []
    queue = deque()
    queue.append(x)
    check[x] = 1
    distance[x] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)
                distance[i] += distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
bfs(x)