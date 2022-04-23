# BOJ 1439
S = input()
newS = S[0]
for s in range(1, len(S)):
    if newS[-1] == S[s]:
        continue
    else:
        newS += S[s]

j = len(newS)-1
count = 0
while True:
    if len(newS) == 1:
        break
    else:
        if newS[0] == newS[j]:  # 처음과 끝이 똑같다면
            newS = newS[1:-1]  # 처음과 끝 자르기
            count += 1
            j -= 2
        elif newS[0] != newS[j]:  # 처음과 끝이 다르다면
            newS = newS[1:]  # 맨 앞만 자르기 newS[0:-1]도 무방
            count += 1
            j -= 1
print(count)

