n, m = map(int, input().split())
cards = []
for _ in range(n):
    row = list(map(int, input().split()))
    row.sort()
    cards.append(row)
cards = sorted(cards, key=lambda x: x[0])
# print(cards)
print(cards[n-1][0])