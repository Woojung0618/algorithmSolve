def solution(record):
    answer = []
    id_name = dict()  # {'id': 'name'}
    result = []  # id + 들어오고 나가고 기록
    for r in record:
        arr = r.split()
        if arr[0] == 'Enter':
            id_name[arr[1]] = arr[2]
            result.append(arr[1])
            result.append('님이 들어왔습니다.')
        elif arr[0] == 'Change':
            id_name[arr[1]] = arr[2]
        else:
            result.append(arr[1])
            result.append('님이 나갔습니다.')
    ans = ''
    for res in result:
        if res[0] != '님':
            ans += id_name[res]
        else:
            ans += res
            answer.append(ans)
            ans = ''
        
    return answer