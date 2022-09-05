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

# 방문하지 않은 노드 중, 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리(cost)가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

결과
0
2
3
1
2
4
-> 1번 노드에서 출발했을 때, 2~6번까지의 최단 경로
'''