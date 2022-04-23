# 또 다른 풀이
# 가장 큰 수, 두번째로 큰 수의 더해지는 개수를 구해서 더하는 방법
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
first, second = numbers[n-1], numbers[n-2]

count = (m // k) * k
count += m % (k+1)

answer = first * count + second * (m - count)
print(answer)
