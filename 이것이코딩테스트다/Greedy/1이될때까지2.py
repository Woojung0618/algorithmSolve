n, k = map(int, input().split())
count = 0
while True:
    temp = (n // k) * k
    count += (n - temp)
    n = temp

    if n < k:
        break
    count += 1
    n //= k
count += (n - 1)
print(count)
