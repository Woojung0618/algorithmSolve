import sys
n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    data.append([name, int(kor), int(eng), int(math)]) 
data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for d in data:
    print(d[0])