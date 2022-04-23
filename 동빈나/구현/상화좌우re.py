n = int(input())
go = list(input().split())
result = [1, 1]

move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for g in go:
    for i in range(len(move)):
        if g == move[i]:
            nx = result[0] + dx[i]
            ny = result[1] + dy[i]
    if nx > n or nx < 1 or ny > n or ny < 1:
        continue
    else:
        result[0] = nx
        result[1] = ny
print(*result)