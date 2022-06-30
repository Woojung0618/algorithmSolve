def solution(new_id):
    answer = ''
    # 1단계
    id_1 = new_id.lower()
    # 2단계
    for i in id_1:
        if i.isalnum() or i in '._-':
            answer += i
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    # 7단계
    if len(answer) == 1:
        answer = answer * 3
    elif len(answer) == 2:
        answer = answer + answer[1]
    
    return answer