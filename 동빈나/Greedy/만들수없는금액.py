n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

answer = 1
while True:
    number = answer
    if number < coins[n-1]:  # 동전 중 가장 작은 금액보다 작을 경우
        break # -> answer 출력
    for i in range(n):
        if number == 0:  # number == 0 이라면 딱 떨어진 것이므로 만들 수 있는 금액
            break
        if number < coins[i]:  # 다음 coin으로 넘어감
            continue
        else:
            number -= coins[i]  # 큰 수부터 하나씩 뺌
        # 0이 안됐는데 coin 끝까지 다 왔다 -> 그러면 answer 출력해야함
        if number != 0 and i == n-1:
            print(answer)
            exit(0)
    answer += 1

print(answer)