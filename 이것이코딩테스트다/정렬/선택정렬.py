'''
[선택정렬]
정렬되지 않은 데이터 중 가장 작은 값을 '선택'하여 '맨앞'으로 보낸다.

시간복잡도 O(n^2)
데이터가 10000개 이상일 경우 적절X
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i  # min_index: 최솟값을 찾기 위한 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 최솟값과 맨앞을 swap
print(array)