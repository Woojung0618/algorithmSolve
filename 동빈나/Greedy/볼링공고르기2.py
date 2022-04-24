# combinations 없이 풀기
n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 1부터 10까지 무게를 담을 수 있는 리스트
array = [0] * 11
for x in balls:
    array[x] += 1

result = 0
# 1부터 m까지 각 무게에 대해 처리
for i in range(1, m+1):
    n -= array[i]  # 무게가 i 인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  # B가 선택한 개수(array[i])와 A가 선택한 개수(n)를 곱
print(result)