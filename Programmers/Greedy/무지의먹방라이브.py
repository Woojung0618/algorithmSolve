import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []  # 시간이 적은 음식부터 빼야 하므로 우선순위 큐 이용(최소힙)
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (음식 시간, 음식 번호)
    
    n = len(food_times)
    previous = 0  # 이전에 제거한 음식의 food_time

    while q:
        # 먹는데 걸리는 시간 = (남은 양) * (남은 음식 개수)
        eat_time = (q[0][0] - previous) * n

        #시간이 남을 경우 현재 음식 빼기
        if k >= eat_time:
            k -= eat_time
            previous = heapq.heappop(q)[0]
            n -= 1
        
        # 시간이 부족할 경우 남은 음식 중 먹을 음식 색출
        else:
            i = k % n
            q.sort(key=lambda x: x[1])
            return q[i][1]



print(solution([8, 6, 4], 15))
print(solution([3, 1, 2], 5))