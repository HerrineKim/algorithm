from collections import deque

def sliding_window_minimum(N, L, A):
    # 결과를 저장할 리스트
    result = []
    # 덱을 사용하여 슬라이딩 윈도우에서 최솟값 관리
    dq = deque()

    for i in range(N):
        # 덱의 앞쪽 값이 윈도우 범위에서 벗어나면 제거
        if dq and dq[0] < i - L + 1:
            dq.popleft()
        
        # 덱의 뒷쪽 값이 새로 들어올 값보다 크면 제거
        while dq and A[dq[-1]] > A[i]:
            dq.pop()
        
        # 현재 인덱스를 덱에 추가
        dq.append(i)
        
        # 결과에 현재 윈도우에서의 최솟값 추가
        result.append(A[dq[0]])

    return result

# 입력 받기
N, L = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
result = sliding_window_minimum(N, L, A)
print(" ".join(map(str, result)))