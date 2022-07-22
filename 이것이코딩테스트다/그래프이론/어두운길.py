import sys
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
info = []
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i  # parent 초기화

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    info.append((z, x, y))  # z: cost, x,y: 집 번호
info.sort()

result = 0
ans = 0
for x in info:
    cost, x, y = x
    if find_parent(parent, x) != find_parent(parent, y):  # cycle 없는 경우
        union_parent(parent, x, y)
        ans += cost
    result += cost
print(result - ans)

'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
