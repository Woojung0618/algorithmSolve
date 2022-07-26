import sys
n = int(input())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array = sorted(array)
for i in array:
    print(i)