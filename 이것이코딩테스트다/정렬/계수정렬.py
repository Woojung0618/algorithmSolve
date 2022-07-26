'''
[계수정렬]
주어진 데이터 크기 k만큼의 새로운 리스트 선언.
리스트에 각 데이터가 몇번 등장했는지 횟수 기록.
(제한 조건 : 데이터의 크기 범위가 제한되어 정수로 표현할 수 있을 때)

시간복잡도 O(n+k)
공간복잡도 O(n+k) 주의
'''
array = [7, 5, 9, 0, 3, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1)  # 모든 범위를 포함하는 리스트 선언
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')