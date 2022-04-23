n, m = map(int, input().split())
x, y, d = map(int, input().split())  # 현재 위치, 방향
map_list = []
for _ in range(n):
    map_list.append(list(map(int, input().split())))
memo = [[0] * m for _ in range(n)]  # 방문 여부 표시

dx = [-1, 0, 1, 0]  # 북=0(좌) 동=1(하) 남=2(우) 서=3(상)
dy = [0, 1, 0, -1]
count = 1
turn_time = 0

while True:
    # 왼쪽으로 돌기
    d += 1
    if d == 4:
        d = 0

    nx = x + dx[d]
    ny = y + dy[d]

    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
    if memo[nx][ny] == 0 and map_list[nx][ny] == 0:
        count += 1
        memo[nx][ny] = 1
        turn_time = 0
        x, y = nx, ny
        continue

    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동하기
        if map_list[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)