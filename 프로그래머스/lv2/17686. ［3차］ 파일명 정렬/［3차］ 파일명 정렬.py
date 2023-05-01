def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        number_check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                number_check = True
            elif number_check:
                tail = file[i:]
                break
            else:
                head += file[i]
        answer.append((head, number, tail))
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(x) for x in answer]

    return answer
