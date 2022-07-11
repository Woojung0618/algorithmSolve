def check(w):
    if w == '':
        return True
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == ')':
                stack.append(i)
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    
def sep_uv(w):
    if w == '':
        return ''
    stack = [w[0]]
    cnt = 0
    
    for i in w[1:]:
        if len(stack) == 0:
            break
        if stack[-1] == i:
            stack.append(i)
        else:
            stack.pop()
        cnt += 1
    u = w[:cnt+1]
    v = w[cnt+1:]
    # print('u', u)
    # print('v', v)
    if check(u): # stage 3
        return u + sep_uv(v)
    else: # stage 4
        u = u[1:-1]
        u = u[::-1]
        return '(' + sep_uv(v) + ')' + u
    
    
def solution(p):
    return sep_uv(p)