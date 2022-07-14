from collections import deque
n, k = map(int, input().split())
visit = [0] * 100001
def bfs(s):
    queue = deque([s])
    visit[s] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            return visit[k]
        if x < 100000 and visit[x+1] == 0:
            visit[x+1] = visit[x] + 1
            queue.append(x+1)
        if x > 0 and visit[x-1] == 0:
            visit[x-1] = visit[x] + 1
            queue.append(x-1)
        if x * 2 <= 100000 and visit[x*2] == 0:
            visit[x*2] = visit[x] + 1
            queue.append(x*2)

print(bfs(n))

# 처음 dfs로 접근함 -> fail (무한루프)
# answer = sys.maxsize
# def dfs(start, end, time):
#     global answer
#     if start == end:
#         answer = min(answer, time)
#         return 
#     if start-1 >= 0:
#         dfs(start-1, end, time+1)
#     if start+1 <= 100000:
#         dfs(start+1, end, time+1)
#     if start*2 <= 100000:
#         dfs(start*2, end, time+1)
# dfs(n ,k, 0)
# print(answer)