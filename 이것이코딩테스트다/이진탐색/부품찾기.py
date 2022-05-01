import sys
n = int(input())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] < target:
        start = mid + 1
        return binary_search(array, target, start, end)
    elif array[mid] > target:
        end = mid - 1
        return binary_search(array, target, start, end)
    
for num in m_list:
    print(binary_search(n_list, num, 0, n-1), end=' ')
