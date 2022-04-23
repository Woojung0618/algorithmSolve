n = int(input())
TIME = 60
count = 0

for h in range(n+1):
    for i in range(TIME):
        for j in range(TIME):
            if '3' in str(h) or '3' in str(i) or '3' in str(j):
                count += 1
print(count)