from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    table = {}  # {'메뉴': 횟수}
    # 가능한 모든 조합 생성해서 table에 넣기
    for order in orders:
        combi = []
        order = sorted(order) # 순서 다른거 확인하려면 -> 알파벳으로 정렬
        for i in course:
            combi.extend([''.join(x) for x in combinations(order, i)])
        for com in combi:
            if table.get(com) == None:
                table[com] = 1
            else:
                table[com] += 1
    filter_tab = dict(filter(lambda x: x[1]>=2, table.items()))
    sort_tab = dict(sorted(filter_tab.items(), reverse=True, key=lambda x: x[1]))
    print(sort_tab)
    # 동일 value 값 중에서 key의 개수가 가장 많은 것들 리턴
    for c in course:
        key_dict = list(dict(filter(lambda x: x[1] == c, sort_tab.items())).keys())
        max_count = 0
        for a in key_dict:
            if len(a) > max_count:
                max_count = len(a)
        final_dict = list(filter(lambda x: len(x) == max_count, key_dict))
        answer.extend(final_dict)
    return sorted(answer)