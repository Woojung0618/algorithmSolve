from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))
combis = list(combinations(balls, 2))

answer = len(combis)
for combi in combis:
    if combi[0] == combi[1]:
        answer -= 1

print(answer) 