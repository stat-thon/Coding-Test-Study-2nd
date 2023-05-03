def solution(n, s, a, b, fares):
    inf = int(10e9)
    graph = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    
    for f in fares:
        graph[f[1] - 1][f[0] - 1] = f[2]
        graph[f[0] - 1][f[1] - 1] = f[2]
        
    # 플로이드 워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return min(graph[s-1][k] + graph[k][a-1] + graph[k][b-1] for k in range(n))
