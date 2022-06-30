def solution(s):
    answer = -1
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0
    
    
    
    # s = list(s)
    # i = 0
    # while len(s) >= 2:
    #     if s[i] == s[i+1]:
    #         del s[i+1]
    #         del s[i]
    #         if i != 0:
    #             i -= 1
    #     else:
    #         i += 1
    #     if i == len(s)-1:
    #         return 0
    # if len(s) == 0:
    #     return 1
    # else:
    #     return 0

    # return answer