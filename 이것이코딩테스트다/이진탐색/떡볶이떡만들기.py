import sys
n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    # 떡의 합이 m 되는지 check
    value = 0
    for i in array:
        if i > mid:
            value += i - mid
    # 떡의 합이 m보다 작으면 더 많이 잘라야하니까 end를 줄이기
    if value < m:
        end = mid - 1
    # 떡의 합이 m보다 크면 충분한 거니까 일단 answer 기록하고, start 늘리기
    else:
        answer = mid
        start = mid + 1
        
print(answer)

