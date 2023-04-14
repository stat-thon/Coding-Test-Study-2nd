from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    q = deque([1])
    dist = [-1 for _ in range(n+1)]
    dist[1] = 0
    while q:
        a = q.popleft()
        for i in graph[a]:
            if dist[i] == -1:
                dist[i] = dist[a] + 1
                q.append(i)
    
    return dist.count(max(dist))
