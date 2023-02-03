def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key = len)
    # print(s)
    for i in s:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer