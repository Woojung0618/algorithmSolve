import sys
from itertools import combinations
def calc_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
n, m = map(int, input().split())
maps = []
chickens = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    maps.append(row)
    for j in range(n):
        if row[j] == 2:
            chickens.append((i, j))

combi = list(combinations(chickens, m))
# print(combi)

answer = sys.maxsize
for com in combi:
    result = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                mindist = sys.maxsize
                for c in com:    
                    mindist = min(calc_dist(i, j, c[0], c[1]), mindist)
                result += mindist
    answer = min(answer, result)
print(answer)