def solution(n, words):
    answer = []
    record = [words[0]]
    for i in range(1, len(words)):
        if words[i] in record:
            return [i%n + 1, i//n + 1]
        if record[-1][-1] != words[i][0]:
            return [i%n + 1, i//n + 1]
        record.append(words[i])
    return [0, 0]