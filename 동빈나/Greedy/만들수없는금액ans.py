n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    print('target', target)
    print('x', x)
    # 만들 수 없는 금액을 찾으면 반복 종료
    if target < x:
        break
    target += x

print(target)