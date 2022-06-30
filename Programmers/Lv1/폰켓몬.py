def solution(nums):
    answer = 0
    N = len(nums)
    M = N//2
    pons = set(nums)
    if len(pons) >= M:
        return M
    return len(pons)