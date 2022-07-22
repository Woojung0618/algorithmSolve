from collections import deque 

v, e = map(int, input().split())
indegree = [0] * (v+1)  # 모든 노드의 진입차수 0으로 초기화
graph = [[] for i in range(v+1)]  # 각 노드의 간선 정보를 담을 연결 리스트 초기화

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬
def topology_sort():
    result = []
    q = deque()

    # 처음에 진입차수=0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        # now 와 연결딘 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()