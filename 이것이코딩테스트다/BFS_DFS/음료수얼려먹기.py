n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 벗어날 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 현재 노드 방문하지 않았다면
        graph[x][y] = 1 # 방문 처리
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        # 연결된 모든 지점을 방문한 다음에 True 반환
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1
print(result)