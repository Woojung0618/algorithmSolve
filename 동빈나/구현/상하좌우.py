n = int(input())
go = list(input().split())
result = [1, 1]

for g in go:
    if g == 'L':
        if result[1] == 1:
            continue
        else:
            result[1] -= 1
    elif g == 'R':
        if result[1] == n:
            continue
        else:
            result[1] += 1
    elif g == 'U':
        if result[0] == 1:
            continue
        else:
            result[0] -= 1
    elif g == 'D':
        if result[0] == n:
            continue
        else:
            result[0] += 1
print(*result)