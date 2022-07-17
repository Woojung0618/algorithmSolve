import sys
from collections import deque
import copy

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().split()))
# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 브루트포스로 3군데 세워놓고, bfs 돌리기
check = True 
# 경우들 돌면서 모든 경우에 S 마주치면 False (NO)
# 한번이라도 안마주치고 True가 나오면 True (YES) 출력하고 끝

def install(cnt):
    if cnt == 3:
        if bfs():
            print('YES')
            exit(0)
        else:
            return
       
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                install(cnt+1)
                graph[i][j] = 'X'

def bfs():
    temp = copy.deepcopy(graph)
    # print('----------------------------------------')
    # for i in range(n):
    #     print(temp[i])
    queue = deque()
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 'T':
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            while 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] == 'S':
                    # print('**********False**********')
                    return False
                elif temp[nx][ny] == 'X':
                    nx += dx[i]
                    ny += dy[i]
                else:
                    break
    # print('True')
    return True

install(0)
print('NO')

'''
5
X X S X X
X X X X X
S X T X S
X X X X X
X X S X X
NO
'''
