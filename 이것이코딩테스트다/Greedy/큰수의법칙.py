n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(numbers, reverse=True)

answer = 0

# 제일 큰 수를 k번 더하고, 두번째 큰 수를 1번, 그 다음 또 반복..
while m:
    if m >= k + 1:
        answer += k * numbers[0] + numbers[1]
        m -= k + 1
    else:
        answer += m * numbers[0]
        m = 0
print(answer)