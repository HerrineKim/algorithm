def solution(numbers):
    # 으하하 짜증나.. 11번
    # if 0 == sum(numbers):
    #     return "0"
    
    from functools import cmp_to_key
    
    answer = "".join(sorted(list(map(str, numbers)), key=cmp_to_key(str_num_compare), reverse=True))
    
    # 이게 좀 낫네
    answer = answer.lstrip("0") # 아니 다 지워지면 안돼지..ㅠ
    answer = '0' if len(answer) == 0 else answer
    
    return answer

# 뭐지 : 테스트 11 〉	실패 (0.06ms, 10.3MB) 으하하 0..

def str_num_compare(x, y):
    if int(x + y) < int(y + x):
        return -1
    elif int(x + y) > int(y + x):
        return 1
    else: 
        return 0