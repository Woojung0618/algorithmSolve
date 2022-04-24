import sys
def solution(employees, n):
    answer = n
    employees.sort(key=lambda x: x[0])
    rank = employees[0][1]
    for i in range(1, n):
        if employees[i][1] > rank:
            answer -= 1
        else:
            rank = employees[i][1]
    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    employees = []
    for _ in range(N):
        s1, s2 = map(int, sys.stdin.readline().split())
        employees.append([s1, s2])
    print(solution(employees, len(employees)))
