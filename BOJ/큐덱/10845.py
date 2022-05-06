import sys
n = int(input())
queue = []
for _ in range(n):
    m = sys.stdin.readline().rstrip()
    if m == 'size':
        print(len(queue))
    elif m == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif m == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif m == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif m == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    else:
        p, num = m.split()
        queue.append(num)