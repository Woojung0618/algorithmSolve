from collections import deque
import copy

n = int(input())
time = [0] * (n+1)
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for v in range(1, n+1):
    t = list(map(int, input().split()))
    time[v] = t[0]
    for i in t[1:-1]:
        graph[i].append(v)
        indegree[v] += 1

def topology():
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+time[i])
            if indegree[i] == 0:
                q.append(i)
            
    print(result)
topology()
'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''