'''
[퀵정렬]
pivot을 기준으로 좌측과 우측을 정렬

시간복잡도 O(nlogn)
'''
array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_python(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)
print(quick_sort_python(array1))

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개일 경우 리턴
        return
    pivot = start  # pivot은 첫 번째 원소
    left, right = start+1, end
    while left <= right:
        # pivot보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 pivot과 작은 데이터를 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 좌측, 우측에서 각각 퀵 소트 진행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array2, 0, len(array2)-1)
print(array2)

