import sys
def solution(s):
    n = len(s)
    if n == 1:
        return 1
    MAX = n // 2
    MIN = sys.maxsize
    for i in range(MAX, 0, -1):
        array = []
        for j in range(n//i):
            array.append(s[j*i:j*i+i])
        if n % i != 0:
            array.append(s[(n//i)*i:])
        same_cnt = 1
        result = ''
        # print(array)
        for a in range(len(array)-1):                
            if array[a] == array[a+1]:
                same_cnt += 1
            else:
                if same_cnt > 1:
                    result += str(same_cnt) + array[a]
                    same_cnt = 1
                else:
                    result += array[a]
        if same_cnt > 1:
            result += str(same_cnt) + array[-1]
        else:
            result += array[-1]
        
        L = len(result)
        if MIN > L:
            answer = L
            MIN = answer
            
    return answer