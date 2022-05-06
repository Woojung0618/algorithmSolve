# R (뒤집기) 횟수가 홀수일 때만 reverse() 사용하여 시간초과 나지 않게
# D (삭제) : R에 따라 front, back 변수를 1씩 증가시켜 
# 마지막에 error 나지 않는 경우에만 계산하도록
import sys
from collections import deque
T = int(input())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    x = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    rev = 0
    front, back = 0, 0
    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(x) > 0:
                if rev % 2 == 0:
                    front += 1
                else:
                    back += 1

    if front + back <= n:
        for _ in range(front):
            x.popleft()
        for _ in range(back):
            x.pop()

        if rev % 2 != 0:
            x.reverse()
        print('['+','.join(x)+']')
    else:
        print('error')