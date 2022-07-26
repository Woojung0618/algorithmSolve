'''
[삽입정렬]
특정 데이터를 적절한 위치에 '삽입'한다. 
삽입되는 위치 앞까지는 모두 정렬되어 있다는 가정. 대부분 정렬되어 있는 데이터에서 특정 데이터를 삽입할 때 유리

시간복잡도 O(n^2). 최선의 경우(거의 정렬되어 있는 경우) O(n)
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i부터 한칸씩 앞으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]  # 한칸씩 이동
        else:  # 자기보다 작은 애를 만나면
            break  # 해당 위치에 삽입
print(array)