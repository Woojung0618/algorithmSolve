
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

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union_parent(parent, i+1, j+1)
print(parent)
# union_parent 후 부모가 같은지 여부 확인
# 모두 같으면 YES
# 다른 게 하나라도 있으면 NO
quest = list(map(int, input().split()))
result = 'YES'
for q in range(1, len(quest)-1):
    if find_parent(parent, q) != find_parent(parent, q+1):
        result = 'NO'
print(result)


'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''