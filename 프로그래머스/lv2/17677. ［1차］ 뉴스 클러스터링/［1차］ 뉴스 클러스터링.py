def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i]+str1[i + 1])
            
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i] + str2[i + 1])
            
    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536
    
    str1_set = set(str1_list)
    str2_set = set(str2_list)
    
    gyo = str1_set & str2_set
    print(gyo)
    
    hap = str1_set | str2_set
    print(hap)
    gyo_cnt = 0
    hap_cnt = 0
    
    for x in gyo:
        gyo_cnt += min(str1_list.count(x), str2_list.count(x))
    
    for y in hap:
        hap_cnt += max(str1_list.count(y), str2_list.count(y))
        
    answer = int((gyo_cnt / hap_cnt) * 65536)
    
    return answer
