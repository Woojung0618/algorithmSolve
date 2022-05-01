import sys
k, n = map(int, input().split())
array = [int(sys.stdin.readline().strip()) for _ in range(k)]

start = 1
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2

    # total 값 구하기
    for x in array:
        total += x // mid

    # total 비교해서 start, end 조정
    if total < n: # total이 적은거면, 너무 크게 자른거니까, end 줄여야함
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)