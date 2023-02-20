def dfs(tickets, start, visited, path):
    if len(path) == len(tickets) + 1:
        return path

    for i, ticket in enumerate(tickets):
        if ticket[0] == start and not visited[i]:
            visited[i] = True
            path.append(ticket[1])
            dfs(tickets, ticket[1], visited, path)
            if len(path) == len(tickets) + 1:
                return path
            path.pop()
            visited[i] = False

def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: x[0])
    answer = dfs(tickets, "ICN", visited, ["ICN"])

    return answer

# def bfs(tickets, start, visited, path):
#     if len(path) == len(tickets) + 1:
#         return path
#     for i in range(len(tickets)):
#         if tickets[i][0] == start and not visited[i]:
#             visited[i] = True
#             path.append(tickets[i][1])
#             path = bfs(tickets, tickets[i][1], visited, path)
#             if len(path) == len(tickets) + 1:
#                 return path
#             visited[i] = False
#             path.pop()
#     return path

# def solution(tickets):
#     answer = []
#     visited = [False] * len(tickets)
#     tickets.sort()
#     answer = bfs(tickets, "ICN", visited, ["ICN"])

#     return answer