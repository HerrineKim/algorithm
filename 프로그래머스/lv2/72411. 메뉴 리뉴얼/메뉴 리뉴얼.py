from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    # 메뉴들의 길이 별로 조합 구하기
    for c in course:
        temp = []
        # 각 주문별로 조합 만들기
        for order in orders:
            temp += combinations(sorted(order), c)
        counter = Counter(temp)
        # print(counter)
        if len(counter) >= 1:
            answer.extend([''.join(key) for key in counter if counter[key] == max(counter.values()) and counter[key] >= 2])
    return sorted(answer)