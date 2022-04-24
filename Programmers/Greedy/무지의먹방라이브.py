import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []  # �ð��� ���� ���ĺ��� ���� �ϹǷ� �켱���� ť �̿�(�ּ���)
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (���� �ð�, ���� ��ȣ)
    
    n = len(food_times)
    previous = 0  # ������ ������ ������ food_time

    while q:
        # �Դµ� �ɸ��� �ð� = (���� ��) * (���� ���� ����)
        eat_time = (q[0][0] - previous) * n

        #�ð��� ���� ��� ���� ���� ����
        if k >= eat_time:
            k -= eat_time
            previous = heapq.heappop(q)[0]
            n -= 1
        
        # �ð��� ������ ��� ���� ���� �� ���� ���� ����
        else:
            i = k % n
            q.sort(key=lambda x: x[1])
            return q[i][1]



print(solution([8, 6, 4], 15))
print(solution([3, 1, 2], 5))