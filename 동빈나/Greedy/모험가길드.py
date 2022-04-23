n = int(input())
x = list(map(int, input().split()))
x.sort()  

answer = 0
idx = 0  # 현재 사람의 인덱스
while True:
    num = x[idx]  # 현재 사람의 공포도
    answer += 1
    if idx + num >= n:  # 현재 사람의 공포도만큼 수 추가
        break  # 만약 n을 넘어가면 break
    else:  # 현재 사람의 공포도만큼 인원 수를 추가했을 때 n을 넘지 않는다면 
        idx += num  # idx 조정하여 다음 사람 따지도록

print(answer)