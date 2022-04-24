n = int(input())
people = list(map(int, input().split()))
answer = 0
people.sort()
for i in range(len(people)):
    sum_value = sum(people[:i+1])
    answer += sum_value
print(answer)