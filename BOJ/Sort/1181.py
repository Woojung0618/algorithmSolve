import sys
n = int(input())
array = []
words = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in words:
        array.append((word, len(word)))
    words.append(word)
array = sorted(array, key=lambda x: (x[1], x[0]))

for i in array:
    print(i[0])