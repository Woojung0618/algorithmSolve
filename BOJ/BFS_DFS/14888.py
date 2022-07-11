import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
MAX, MIN = -sys.maxsize, sys.maxsize

def dfs(depth, nums, plus, minus, multi, div, result):
    global MAX, MIN
    if depth == n-1:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    
    if plus:
        dfs(depth+1, nums, plus-1, minus, multi, div, result + nums[depth+1])
    if minus:
        dfs(depth+1, nums, plus, minus-1, multi, div, result - nums[depth+1])
    if multi:
        dfs(depth+1, nums, plus, minus, multi-1, div, result * nums[depth+1])
    if div:
        if result < 0:
            temp = (result * (-1)) // nums[depth+1]
            dfs(depth+1, nums, plus, minus, multi, div-1, temp * -1)
        else:
            dfs(depth+1, nums, plus, minus, multi, div-1, result // nums[depth+1])

dfs(0, nums, op[0], op[1], op[2], op[3], nums[0])
print(MAX)
print(MIN)