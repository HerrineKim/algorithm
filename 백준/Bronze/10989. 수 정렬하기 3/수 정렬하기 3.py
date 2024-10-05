import sys # 빠른 입력을 위한 sys 모듈 가져오기

li = [0 for _ in range(10001)] # counting sort에서 빈도 저장하기 위한 배열

N = int(sys.stdin.readline()) # 숫자를 입력 받는다.

for _ in range(N): # N을 순회하면서
    num = int(sys.stdin.readline()) # 인풋으로 받은 수가
    li[num] += 1 #  몇 번 들어왔는지 빈도를 저장한다.

# counting sort
for i in range(1, 10001): # 빈도 배열을 순회하면서
    count = li[i] 
    for _ in range(count): 
        print(i) # 저장된 빈도만큼 각 값을 출력한다.