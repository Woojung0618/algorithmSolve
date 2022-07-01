def solution(s):
    answer = []
    s = s[2:]
    s = s[:-2]
    s = s.split('},{')
    # 짧은 것부터 순서대로 정렬
    s_arr = sorted(s, key=lambda x: len(x))
    answer.append(int(s_arr[0]))
    for i in range(1, len(s_arr)):
        nums = s_arr[i].split(',')
        for num in nums:
            num = int(num)
            if num not in answer:
                answer.append(num)
                break

    return answer