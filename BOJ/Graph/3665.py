import sys
from collections import deque
T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())  # 팀 수
    t = list(map(int, sys.stdin.readline().split()))  # 작년 등수
    m = int(sys.stdin.readline())  # change 수
    change = []  # 등수 바뀐 쌍의 수
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        change.append((a, b))

    edges = []  # 그래프 -> 간선
    for i in range(n-1):
        for j in range(i+1, n):
            a, b = t[i], t[j]
            if (a, b) in change or (b, a) in change:  # 간선 순서 바꾸기
                edges.append((b ,a))
            else:
                edges.append((a, b))
    # print('edges', edges)
    # 간선 -> 그래프
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
    # print('graph', graph)
    indegree = [0] * (n+1)
    q = deque()
    # indegree 초기화
    for edge in edges:
        a, b = edge
        indegree[b] += 1
    # print('indegree', indegree)
    # indegree=0 인 것들 q에 push
    for d in range(1, n+1):
        if indegree[d] == 0:
            q.append(d)
    answer = []
    
    if len(q) == 0:
        print('IMPOSSIBLE')
        break
    while q:
        if len(q) > 1: # indegree가 같은 게 여러개 => 답이 여러개 될 수 있음
            print('?')
            break
        now = q.popleft()
        answer.append(now)
        # now와 관련 있는 애들 -1 indegree
        for i in graph[now]:
            indegree[i] -= 1
            print('indegree', indegree)
            if indegree[i] == 0:
                q.append(i)
    if len(answer) != n:
        print('IMPOSSIBLE')
        break
    # print('=>', answer)
    for a in answer:
        print(a, end=' ')
