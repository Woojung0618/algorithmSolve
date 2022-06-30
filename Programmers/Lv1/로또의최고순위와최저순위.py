def solution(lottos, win_nums):
    # 0 제외 맞는 숫자들 개수 구하고
    # 0 개수 +-
    zero = 0
    count = 0
    for lot in lottos:
        if lot == 0:
            zero += 1
        elif lot in win_nums:
            count += 1
    print('맞은개수',count, ' zero',zero)
    first, second = 7-(count + zero), 7-count  # 번호 개수 -> 등수
    if first == 7:
        first = 6
    if second == 7:
        second = 6
    answer = [first, second]
    return answer