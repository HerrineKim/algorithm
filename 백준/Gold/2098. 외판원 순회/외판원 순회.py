import sys

# 무한대를 표현하기 위한 값 설정
INF = float('inf')

def main():
    input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
    n = int(input())  # 도시의 개수를 입력받습니다.
    
    # 비용 행렬을 입력받습니다.
    cost = [list(map(int, input().split())) for _ in range(n)]
    
    # DP 테이블 초기화: dp[visited][i]는 특정 방문 상태에서 현재 도시 i에 있을 때의 최소 비용을 저장합니다.
    dp = [[INF] * n for _ in range(1 << n)]
    
    # 시작 도시에서 시작하는 경우의 비용은 0입니다.
    dp[1][0] = 0
    
    # 모든 상태를 탐색합니다.
    for visited in range(1 << n):
        for current in range(n):
            # 현재 도시가 방문된 상태가 아니라면 건너뜁니다.
            if not (visited & (1 << current)):
                continue
            
            # 현재 도시에서 다른 모든 도시로 이동하는 경우를 고려합니다.
            for next_city in range(n):
                if visited & (1 << next_city):  # 이미 방문한 도시라면 건너뜁니다.
                    continue
                if cost[current][next_city] == 0:  # 갈 수 없는 경우라면 건너뜁니다.
                    continue
                
                next_visited = visited | (1 << next_city)  # 다음 도시 방문 상태를 설정합니다.
                dp[next_visited][next_city] = min(dp[next_visited][next_city], dp[visited][current] + cost[current][next_city])
    
    # 모든 도시를 방문하고 다시 시작점(0번 도시)으로 돌아오는 최소 비용을 찾습니다.
    answer = INF
    for i in range(1, n):
        if cost[i][0] != 0:  # 시작점으로 돌아올 수 있는 경우만 고려합니다.
            answer = min(answer, dp[(1 << n) - 1][i] + cost[i][0])
    
    # 최소 비용을 출력합니다.
    print(answer)

main()