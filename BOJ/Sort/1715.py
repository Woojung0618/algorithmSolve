import sys
import heapq
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))
result = 0
temp = 0
while True:
    if len(heap) == 1:
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    temp = a+b
    result += temp
    heapq.heappush(heap, temp)
print(result)