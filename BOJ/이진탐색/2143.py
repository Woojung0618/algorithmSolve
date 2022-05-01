import sys
T = int(input())
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))

# A에서 가능한 모든 부분합 -> T-A 값이 되는 B의 부분합

# 누적합 배열 sum_array
# i부터 j까지의 누적합 : sum_array[j] - sum_array[i-1]
# 위 내용이 누적합 기초 구현인데, 이 문제에서 이렇게 하면 시간초과 발생
# -> sum(list[i:j+1]) 이렇게 누적합을 구하자


# A의 가능한 누적합들을 넣어놓은 sumA
# B의 가능한 누적합들을 넣어놓은 sumB
sumA, sumB = [], []
for i in range(n):  # O(n^2)
    s = A[i]
    sumA.append(s)
    for j in range(i+1, n):
        s += A[j]
        sumA.append(s)
for i in range(m):  # O(n^2)
    s = B[i]
    sumB.append(s)
    for j in range(i+1, m):
        s += B[j]
        sumB.append(s)

# 이분탐색으로 sumB에 T-sumA 값이 있는지 탐색
# 이분탐색 찾으면 1, 없으면 0 반환하는 걸로 하면 틀림 -> sumB에 해당 값 여러개 있을 수 있는데 하나만 찾고 1 반환하니까
# -> bisect 라이브러리 사용
import bisect
sumA.sort()
sumB.sort()
answer = 0

for i in range(len(sumA)):
    left = bisect.bisect_left(sumB, T - sumA[i])
    right = bisect.bisect_right(sumB, T - sumA[i])
    answer += right - left 
print(answer)