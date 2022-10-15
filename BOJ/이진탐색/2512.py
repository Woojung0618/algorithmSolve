n = int(input())
global country
global limit
country = list(map(int, input().split()))
limit = int(input())

def calc(mid):
    result = 0
    for c in country:
        if c <= mid:
            result += c
        else:
            result += mid
    return result

country.sort()
start, end = 0, country[-1]

while start <= end:
    mid = (start + end) // 2
    if calc(mid) <= limit:
        start = mid + 1
    else:
        end = mid - 1

print(mid, start, end)  # mid 말고 end
