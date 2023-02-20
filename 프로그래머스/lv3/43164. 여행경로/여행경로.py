def dfs(tickets, start, visited, path):
    if len(path) == len(tickets) + 1:
        return path

    for i, ticket in enumerate(tickets):
        if ticket[0] == start and not visited[i]:
						# 가본 적 없는 곳이라면 visit 처리하고 
            visited[i] = True
            path.append(ticket[1])
            dfs(tickets, ticket[1], visited, path)
						# 끝까지 가는데 성공했으면 여태까지 쌓인 path를 return
            if len(path) == len(tickets) + 1:
                return path
						# 쭉 따라 갔는데 잘못 갔다면 pop, unvisit 처리 해주고 다른 path 탐색
            path.pop()
            visited[i] = False

def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
		# ICN 다음으로 올 것으로 알파벳 빠른 것을 놓기 위해 lambda식으로 정렬
    tickets.sort(key=lambda x: x[1])
    answer = dfs(tickets, "ICN", visited, ["ICN"])

    return answer