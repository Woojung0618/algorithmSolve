n = int(input())
meets = []
for _ in range(n):
    meets.append(list(map(int, input().split())))
    

meets.sort(key=lambda x: x[0])  # 시작시간 기준으로 정렬
meets.sort(key=lambda x: x[1])  # 종료시간 기준으로 정렬

now = 0
answer = 0
for meet in meets:
    if now <= meet[0]:
        now = meet[1]
        answer += 1
    else:
        continue
print(answer)