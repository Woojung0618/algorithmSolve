S = input()
S = sorted(S)
numbers = 0
strings = ''
for s in S:
    if s.isdigit():
        numbers += int(s)
    else:
        strings += s

# ���ڰ� ��� 0�� �ڿ� �ٴ� �� ����
if numbers != 0: 
    answer = strings + str(numbers)
else:
    answer = strings

print(answer)