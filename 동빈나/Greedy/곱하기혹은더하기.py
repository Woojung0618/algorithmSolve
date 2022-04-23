S = input()
result = 0
value = int(S[0])

for i in range(1, len(S)):
    value = max(value + int(S[i]), value * int(S[i]))  # 더한 것과 곱한 것 중 큰 값
print(value)