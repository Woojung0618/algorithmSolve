loc = input()
locnum = []
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in range(len(alpha)):
    if loc[0] == alpha[i]:
        locnum = [i+1, int(loc[1])]  # 현재 위치 숫자로 표현

count = 0
for m in range(len(moves)):
    x, y = locnum[0], locnum[1]
    nx = x + moves[m][0]  # nx, ny : 이동하고자 하는 위치
    ny = y + moves[m][1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1
print(count)