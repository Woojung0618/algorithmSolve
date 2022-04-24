N = input()
half = len(N) // 2
left = N[:half]
right = N[half:]

left_value, right_value = 0, 0
for l in left:
    left_value += int(l)
for r in right:
    right_value += int(r)

if left_value == right_value:
    print('LUCKY')
else:
    print('READY')