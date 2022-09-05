import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 10억

n, m = map(int, input().split())   # 노드 개수, 간선 개수
start = int(input())  # 시작 노드
graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보 리스트
visited = [False] * (n+1)  # 방문한 적 있는지 체크하는 리스트
distance = [INF] * (n+1)  # 최단 거리 테이블: INF 으로 초기화

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드까지의 비용 = c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리되었다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 다른 노드들 체크
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리(cost)가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])