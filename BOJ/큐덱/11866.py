import collections
n, k = map(int, input().split())
deq = collections.deque([])
for i in range(n):
    deq.append(i+1)

print('<', end='')
while deq:
    for i in range(k-1):
        deq.append(deq[0])  # 맨 뒤에 맨 앞에 요소 넣고
        deq.popleft()  # 맨 앞에꺼 빼고
    print(deq.popleft(), end='')  # 빠지는 사람 print
    if deq:
        print(', ', end='')
print('>')