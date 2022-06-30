def solution(numbers):
    answer = 0
    arr = [i for i in range(10)]
    for n in arr:
        if n not in numbers:
            answer += n
    return answer