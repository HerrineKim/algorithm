N, K = map(int, input().split())  # N: 배열의 길이, K: K번째 수
A = list(map(int, input().split()))  # 배열 A 입력 받기

A_sorted = sorted(A)  # 배열을 오름차순으로 정렬한다.
print(A_sorted[K-1])  # K번째 수를 출력한다. (1-based 인덱스이므로 K-1)