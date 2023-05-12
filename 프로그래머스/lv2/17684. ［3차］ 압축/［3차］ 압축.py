def solution(msg):
    answer = []
    dic = {}
    # ASCII 코드 활용하여 사전 만들기
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    idx = 27
    i = 0
    while i < len(msg):
        j = i + 1
        while j <= len(msg):
            if msg[i:j] not in dic:
                dic[msg[i:j]] = idx
                idx += 1
                break
            j += 1
        answer.append(dic[msg[i:j - 1]])
        i = j - 1
    return answer