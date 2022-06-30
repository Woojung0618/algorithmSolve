def solution(N, stages):
    answer = []
    fail = {i+1:0 for i in range(N)}  # 실패율 fail[stage번호: 실패율]

    total_cnt = len(stages)
    for i in range(N):
        target = i+1
        fail_cnt = stages.count(target)
        if total_cnt == 0:
            fail[target] = 0
        else:
            fail[target] = fail_cnt/total_cnt
        total_cnt -= fail_cnt
    fail = dict(sorted(fail.items(), reverse=True, key=lambda x: x[1]))

    return list(fail.keys())