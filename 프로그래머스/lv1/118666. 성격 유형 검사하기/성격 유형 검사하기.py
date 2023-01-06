def solution(survey, choices):
    answer = ''
    score = {'A': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'N': 0, 'R': 0, 'T': 0}
    for i in range(len(survey)):
        if choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 5:   
            score[survey[i][1]] += 1
        elif choices[i] == 6:   
            score[survey[i][1]] += 2
        elif choices[i] == 7:   
            score[survey[i][1]] += 3
    print(score)
    # R과 T 비교
    if score['R'] > score['T']:
        answer += 'R'
    elif score['R'] < score['T']:
        answer += 'T'
    else:
        # 사전상 빠른 것
        answer += 'R'
    # C와 F 비교
    if score['C'] > score['F']:
        answer += 'C'
    elif score['C'] < score['F']:
        answer += 'F'
    else:
        answer += 'C'
    # J와 M 비교
    if score['J'] > score['M']:
        answer += 'J'
    elif score['J'] < score['M']:
        answer += 'M'
    else:
        answer += 'J'
    # A와 N 비교
    if score['A'] > score['N']:
        answer += 'A'
    elif score['A'] < score['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer