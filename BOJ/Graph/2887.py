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

def calc_dist(x1, y1, z1, x2, y2, z2):
    return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))

n = int(input())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

edges = []
x_arr, y_arr, z_arr = [], [], []
for i in range(1, n+1):
    x, y, z = map(int, sys.stdin.readline().split())
    x_arr.append((x, i))
    y_arr.append((y, i))
    z_arr.append((z, i))
x_arr.sort()
y_arr.sort()
z_arr.sort()

for i in range(1, n):
    edges.append((abs(x_arr[i][0] - x_arr[i-1][0]), x_arr[i][1], x_arr[i-1][1]))
    edges.append((abs(y_arr[i][0] - y_arr[i-1][0]), y_arr[i][1], y_arr[i-1][1]))
    edges.append((abs(z_arr[i][0] - z_arr[i-1][0]), z_arr[i][1], z_arr[i-1][1]))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
print(result)


'''
주의해야 할 점은 N의 최대 크기가 100,000이므로, 
행성 간 연결할 수 있는 모든 터널을 구할 경우 
메모리 초과가 발생합니다.

따라서, 문제에 주어진 연결 비용 조건인 min(|xA-xB|, |yA-yB|, |zA-zB|)에 따라
 x, y, z 좌표 순으로 행성 좌표를 정렬하여 
 최소가 될 수 있는 간선 정보들만 생성해야 합니다.
'''