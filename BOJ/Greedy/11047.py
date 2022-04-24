n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
answer = 0
for coin in coins:
    if k == 0:
        break
    if k < coin:
        continue
    elif k >= coin:
        q = k // coin
        answer += q
        k -= coin * q
print(answer)