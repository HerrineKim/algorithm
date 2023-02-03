def solution(k, tangerine):
    answer = 0
    num_dict = {}
    for i in range(len(tangerine)):
        if tangerine[i] in num_dict:
            num_dict[tangerine[i]] += 1
        else:
            num_dict[tangerine[i]] = 1
    num_list = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(num_list)):
        if k == 0:
            break
        if k >= num_list[i][1]:
            k -= num_list[i][1]
            answer += 1
        else:
            answer += 1
            break
    return answer