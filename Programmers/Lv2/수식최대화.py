import re

def solution(expression):
    answer = []
    exp = expression
    # exp = re.split('[0-9]', exp)
    # nums = re.split('[-|+|*]', expression)
    all_exp = re.split('([-|+|*])', expression)
    # 6 cases: -+* -*+ +-* +*- *-+ *+-
    calc_order = [['-','+','*'],['-','*','+'],['+','-','*'],['+','*','-'],['*','-','+'],['*','+','-']]
    for order in calc_order:
        target_exp = all_exp.copy()
        for c in order:
            i = 0
            temp = 0
            while i <= len(target_exp) - 1:
                if target_exp[i] == c:
                    a, b = int(target_exp[i-1]), int(target_exp[i+1])
                    if c == '+':
                        temp = a + b
                    elif c == '-':
                        temp = a - b
                    else:
                        temp = a * b
                    for _ in range(3):
                        del target_exp[i-1]
                    target_exp.insert(i-1, str(temp)) # 연산결과 끼워넣기
                    print(target_exp)
                    i -= 1
                i += 1
        if len(target_exp) == 1:
            answer.append(abs(int(target_exp[0])))
    return max(answer)