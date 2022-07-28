import sys
import heapq
n = int(input())
heap = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (s, t))
result = 1
use = []
a, b = heapq.heappop(heap)
heapq.heappush(use, b)
while True:
    if len(heap) == 0:
        break
    a, b = heapq.heappop(heap)
    if use[0] <= a:
        heapq.heappop(use)
    else:
        result += 1
    heapq.heappush(use, b)
print(result)

