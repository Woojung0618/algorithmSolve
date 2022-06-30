def calc_dist(n1, n2): # 두 점의 거리 구하는 함수
    # n1 = 2580
    if n1 == n2:
        return 0
    if n1 == '2':
        if n2 in '135':
            return 1
        elif n2 in '468':
            return 2
        elif n2 in '790':
            return 3
        else:
            return 4
    elif n1 == '5':
        if n2 in '2468':
            return 1
        elif n2 in '13790':
            return 2
        else:
            return 3
    elif n1 == '8':
        if n2 in '5790':
            return 1
        elif n2 in '246*#':
            return 2
        else:
            return 3
    elif n1 == '0':
        if n2 in '8*#':
            return 1
        elif n2 in '579':
            return 2
        elif n2 in '246':
            return 3
        else:
            return 4

def solution(numbers, hand):
    answer = ''
    left_loc = '*'
    right_loc = '#'
    for num in numbers:
        num = str(num)
        if num in '147':  # 왼손
            left_loc += num
            answer += 'L'
        elif num in '369':  # 오른손
            right_loc += num
            answer += 'R'
        else: # 2580 : 1.거리 2.hand
            if calc_dist(num, left_loc[-1]) > calc_dist(num, right_loc[-1]):
                right_loc += num
                answer += 'R'
            elif calc_dist(num, left_loc[-1]) < calc_dist(num, right_loc[-1]):
                left_loc += num
                answer += 'L'
            else:
                if hand == 'right':
                    right_loc += num
                    answer += 'R'
                else:
                    left_loc += num
                    answer += 'L'
    return answer