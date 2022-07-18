from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def nextspots(board, pos, n):
    nextspots = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):  # 상하좌우
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n:
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                nextspots.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2: # 가로 상태
        for i in [-1, 1]:
            if 0 <= x1+i < n and 0 <= x2+i < n:
                if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                    nextspots.append({(x1, y1), (x1+i, y1)})
                    nextspots.append({(x2, y2), (x2+i, y2)})
    elif y1 == y2: # 세로 상태
        for i in [-1, 1]:
            if 0 <= y1+i < n and 0 <= y2+i < n:
                if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                    nextspots.append({(x1, y1), (x1, y1+i)})
                    nextspots.append({(x2, y2), (x2, y2+i)})
    
    return nextspots

def solution(board):
    queue = deque()
    n = len(board)
    visit = []
    start = {(0,0), (0,1)}
    queue.append((start, 0))
    visit.append(start)
    while queue:
        pos, count = queue.popleft()
        if (n-1, n-1) in pos:
            return count
        for nextspot in nextspots(board, pos, n):
            if nextspot not in visit:
                queue.append((nextspot, count+1))
                visit.append(nextspot)
    return 0