def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    arr = [1, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    answer = arr[n - 1]
    return answer % 1234567