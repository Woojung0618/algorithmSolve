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
        if newS[0] == newS[j]:  # ó���� ���� �Ȱ��ٸ�
            newS = newS[1:-1]  # ó���� �� �ڸ���
            count += 1
            j -= 2
        elif newS[0] != newS[j]:  # ó���� ���� �ٸ��ٸ�
            newS = newS[1:]  # �� �ո� �ڸ��� newS[0:-1]�� ����
            count += 1
            j -= 1
print(count)

