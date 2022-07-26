import sys
# 단순히 중앙값을 구하는 문제
n = int(input())
houses = list(map(int, sys.stdin.readline().split()))
houses = sorted(houses)
if n%2 == 1:
    print(houses[n//2])
else:
    print(houses[n//2-1])


# try 1: 계수정렬로 하면 시간초과 안나고 통과될 거라 생각. but 틀림
# k = max(houses)
# count = [0] * (k+1)
# for h in houses:
#     count[h] += 1

# answer = 0
# result = sys.maxsize
# for c in range(len(count)-1):
#     dist = 0
#     for x in range(len(count)-1):
#         dist += abs(c-x) * count[x]
#     if result > dist:
#         answer = c
#         result = dist
# print(answer)
