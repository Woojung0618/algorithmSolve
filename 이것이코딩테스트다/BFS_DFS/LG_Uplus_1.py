# edges = [[0,2], [2,1], [2,4], [3,5], [5,4], [5,7], [7,6], [6,8]]
# n=9
# answer = [2,5]
from itertools import combinations

def dfs(i, cnt):
    for e in remove_edges:
        if e[0] == i:
            j = e[1]
            if visit[j] == 0:
                dfs(j, cnt+1)
                visit[j] = 1
        elif e[1] == i:
            j = e[0]
            if visit[j] == 0:
                dfs(j, cnt+1)
                visit[j] = 1
        return cnt
    return -1

def solution():
    global n
    n = int(input())
    edges = []
    global visit
    global remove_edges
    visit = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges.append([a, b])
    arr = [i for i in range(n)]
    for combi in list(combinations(arr, n-3)):
        answer = []
        remove_edges = []
        print(combi)
        for e in range(0, n-1):
            if e in list(combi):
                remove_edges.append(edges[e])
            else:
                answer.append(e)
        print(remove_edges)
    # dfs 로 leaf node (0)부터 탐색해서 n//3개일때마다 리턴, 마지막에 리턴했을 때 
        count_arr = []
        for i in range(n):
            count = dfs(i, 0)
            print(count)
            if count != n//3:
                continue
            count_arr.append(count)
        if len(count_arr) == 3:
            return answer
solution()

''' edges
0 2
2 1
2 4
3 5
5 4
5 7
7 6
6 8
'''