from collections import deque

def solution(s):
    answer = 0
    x = s[0]
    cnt = 0
    word = deque(s)
    index = 0
    while word:
        if len(word) == 1:
            answer += 1
            break
        if word[index] == x:
            cnt += 1
        else:
            cnt += -1
        if cnt == 0:
            answer += 1
            for i in range(index + 1):
                word.popleft()
            if len(word) == 0:
                # 'aaa' 예외 처리
                if answer == 0:
                    answer += 1
                return answer
            x = word[0]
            index = 0
        else:
            index += 1
            if index == len(word):
                # 'aaa' 예외 처리
                answer += 1
                return answer
        # aaabbaccccabba
        # aaabbacc ccabba
        # ccab ba
        # b a
        # a
    
    return answer