def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        s = 1
        if signs[i] == False:
            s = -1
        answer += absolutes[i] * s
    return answer