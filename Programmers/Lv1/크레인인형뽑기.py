def solution(board, moves):
    answer = 0
    basket = []
    length = len(board)
    for m in moves:
        m -= 1
        i = 0
        # basket에 넣기
        while True:
            if i == length:
                break
            if board[i][m] != 0:
                basket.append(board[i][m])
                board[i][m] = 0
                break
            i += 1
        
        # if 같은 숫자 2개라면 2번 pop, answer+1
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2

    return answer