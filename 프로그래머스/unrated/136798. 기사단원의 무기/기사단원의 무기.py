def solution(number, limit, power):
    answer = 0

    weight_list = [0 for _ in range(number + 1)]

    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            weight_list[j] += 1

    for k in weight_list[1:]:
        if k <= limit:
            answer += k
        else:
            answer += power
    
    return answer