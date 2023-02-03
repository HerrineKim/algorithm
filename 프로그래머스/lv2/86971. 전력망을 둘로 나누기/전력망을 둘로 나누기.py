def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        visited = [0] * (n+1)
        q = [1]
        visited[1] = 1
        cnt = 1
        # print(graph)
        while q:
            node = q.pop()
            for k in graph[node]:
                if visited[k] == 0:
                    visited[k] = 1
                    cnt += 1
                    q.append(k)
        answer = min(answer, abs(n - cnt - cnt))
    return answer