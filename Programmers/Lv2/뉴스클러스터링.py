def solution(str1, str2):
    NUM = 65536
    set1, set2 = [], []
    
    for i in range(len(str1)-1):
        t1 = str1[i:i+2].lower()
        if t1.isalpha():
            set1.append(t1)
    for j in range(len(str2)-1):
        t2 = str2[j:j+2].lower()
        if t2.isalpha():
            set2.append(t2)
    print(set1, set2)
    
    # set1, set2 = [1,1,2,2,3], [1,2,2,4,5]
    # 다중집합
    set_inter = []
    if len(set1) >= len(set2):
        set_temp = set1.copy()
        for i in set2:
            if i in set_temp:
                set_temp.remove(i)
                set_inter.append(i)
        inter = len(set_inter)
        union = len(set2) + len(set_temp)
    else:
        set_temp = set2.copy()
        for i in set1:
            if i in set_temp:
                set_temp.remove(i)
                set_inter.append(i)
        inter = len(set_inter)
        union = len(set1) + len(set_temp)
    
    if union == 0:
        return NUM
    # print('inter',inter, 'union',union)
    
    return int(NUM * (inter/union))