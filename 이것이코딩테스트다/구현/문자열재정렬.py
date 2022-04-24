S = input()
S = sorted(S)
numbers = 0
strings = ''
for s in S:
    if s.isdigit():
        numbers += int(s)
    else:
        strings += s

# 숫자가 없어서 0이 뒤에 붙는 것 방지
if numbers != 0: 
    answer = strings + str(numbers)
else:
    answer = strings

print(answer)