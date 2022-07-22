
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

G = int(input())
P = int(input())

parent = [0] * (G+1)
for i in range(G+1):
    parent[i] = i
# print(parent)

answer = 0
for _ in range(P+1):
    x = int(input())
    temp = find_parent(parent, x)
    if temp == 0:
        break
    union_parent(parent, temp, temp-1)
    answer += 1
print('ans', answer)
exit(0)
'''
4
3
4
1
1
'''
'''
4
6
2
2
3
3
4
4
'''