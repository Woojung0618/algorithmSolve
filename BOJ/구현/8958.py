import sys
def solution(case):
    answer = 0
    previous = 0
    temp = 0
    for c in case:
        if c == 'O':
            if previous == 0:  # O 처음 등장
                temp += 1
                previous = 1
            else:  # O 연속 
                previous += 1
                temp += previous
        else:
            previous = 0
            answer += temp
            temp = 0

    return answer + temp

n = int(input())
for _ in range(n):
    case = sys.stdin.readline()
    print(solution(case))