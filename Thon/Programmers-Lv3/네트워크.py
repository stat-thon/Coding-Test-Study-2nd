def solution(n, computers):
    
    # graph
    n = len(computers)
    graph = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    
    # dfs
    def dfs(node):
        
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)
    
    # result
    visited = [0] * n
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            cnt += 1
    
    return cnt