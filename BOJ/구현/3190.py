import sys
from collections import deque
n = int(input())
maps = [[0]*n for _ in range(n)]

K = int(input())
for _ in range(K):  # 사과의 위치
    a, b = map(int, sys.stdin.readline().rstrip().split())
    maps[a-1][b-1] = 1
L = int(input())
q = deque()
for _ in range(L):  # 뱀의 방향변환 정보
    x, c = sys.stdin.readline().rstrip().split()
    q.append((int(x), c))

i, j = 0, 0
time = 0
d = 0
dy = [1, 0, -1, 0]  # 우 상 좌 하
dx = [0, 1, 0, -1]  # L: -1 D: +1
# 뱀이 지나간 곳 maps = 2로 표시
snake = [(0, 0)]  # 머리, 꼬리
while True:
    i, j = snake[0][0], snake[0][1]  # 머리
    time += 1

    i += dx[d]
    j += dy[d]
    
    if q:
        if time == q[0][0]:
            x, c = q.popleft()
            if c == 'L':
                d -=1
            elif c == 'D':
                d += 1
            if d < 0:
                d = 3
            elif d > 3:
                d = 0        

    if i >= n or j >= n or i < 0 or j < 0 or (i,j) in snake:  # 끝나는 조건
        break
    if maps[i][j] == 0:
        snake.insert(0, (i, j))
        snake.pop()
    elif maps[i][j] == 1:
        snake.insert(0, (i, j))
        maps[i][j] = 0

print(time)

'''
5
2
2 5
2 4
6
4 D
5 D
6 D
7 D
8 D
9 D
답 : 14
반례 -> 사과를 먹었으면 먹었다는 표시
'''