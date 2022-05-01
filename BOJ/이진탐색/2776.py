import sys

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        start = mid + 1
        return binary_search(array, target, start, end)
    elif array[mid] > target:
        end = mid - 1
        return binary_search(array, target, start, end)

T = int(input())
for _ in range(T):
    N = int(input())
    array1 = list(map(int, sys.stdin.readline().rstrip().split()))
    array1.sort()
    M = int(input())
    array2 = list(map(int, sys.stdin.readline().rstrip().split()))



    for x in array2:
        print(binary_search(array1, x, 0, N-1))
