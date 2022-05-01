n, m = map(int, input().split())
array = list(map(int, input().split()))
start = max(array)  # start를 MAX 로 잡기
end = sum(array)

while start <= end:
    mid = (start + end) // 2

    count = 1  # 블루레이 개수
    temp = 0
    for x in array:
        if (mid - temp) >= x:  # x가 이번 블루레이에 들어갈 수 있으면
            temp += x
        else:
            temp = x
            count += 1
    
    # count 개수와 m을 비교하여 start, end 값 조정
    if count > m:  # count가 더 많으면 mid를 너무 작게 잡은 것이므로 start 조정
        start = mid + 1
    else:
        end = mid - 1

    
print(start)