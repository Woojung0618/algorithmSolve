import re
S = input()
numbers = []
operators = []

numbers = re.split('[+-]', S)
for s in S:
    if s == '+' or s == '-':
        operators.append(s)

# previous + now + -> + 로 계산, previous + 그대로
# previous + now - -> - , previous - 로 업데이트
# previous - now + -> - , previous - 그대로
# previous - now - -> - , previous - 그대로

answer = int(numbers[0])
previous = '+'
for i in range(len(operators)):
    now = operators[i]
    if previous == '+':
        if now == '+':
            answer += int(numbers[i+1])
        else:
            answer -= int(numbers[i+1])
            previous = '-'
    else:
            answer -= int(numbers[i+1])
print(answer)