n = input() # 숫자를 입력 받는다.

def fibonacci(n): # 피보나치 수열의 n번째 수를 반환하는 함수를 정의한다.
    if n == 0: # 만약 n이 0이면
        return 0 # 0을 반환한다.
    elif n == 1: # 만약 n이 1이면
        return 1 # 1을 반환한다.
    else: # 그 외 모든 경우에는
        a, b = 0, 1  # 첫 번째와 두 번째 피보나치 수를 0과 1로 설정한다.
        for _ in range(2, n + 1):  # 세 번째 수부터 n번째 수까지 반복문을 사용해
            a, b = b, a + b  # 두 수의 합을 계산하여 다음 피보나치 수를 구한다.
        return b  # 최종적으로 n번째 피보나치 수를 반환한다.

print(fibonacci(int(n))) # 함수를 호출한 결과를 출력한다.