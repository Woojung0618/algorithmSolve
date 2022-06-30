def solution(s):
    arr1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr2 = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(10):
        if arr1[i] in s:
            s = s.replace(arr1[i], arr2[i])
    return int(s)