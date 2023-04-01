def solution(n, edge):
    
    # graph
    from collections import deque, Counter, defaultdict
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    
    # bfs
    visited = [0] * n
    visited[0] = 1
        
    dq = deque()
    dq.append((0, 0))
    
    result = [0] * n
    
    while dq:
            
        q, dist = dq.popleft()
        result[q] = dist
            
        for i in graph[q]:
            
            if visited[i] == 0:
                visited[i] = 1
                dq.append((i, dist + 1))
                
    return Counter(result)[max(result)]