import sys
from collections import deque

n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
group = [[] for _ in range(n+1)]
check = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    group[a].append(b)
    group[b].append(a)

def dfs(a):
    for i in group[a]:
        if check[i] == 0:
            check[i] = check[a] + 1
            dfs(i)

def bfs(a):
    queue = deque()
    queue.append(a)
    while queue:
        x = queue.popleft()
        for i in group[x]:
            if check[i] == 0:
                check[i] = check[x] + 1
                queue.append(i)                    
                

bfs(x)

if check[y] == 0:
    print(-1)
else:
    print(check[y])