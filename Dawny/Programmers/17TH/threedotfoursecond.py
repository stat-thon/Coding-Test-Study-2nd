from collections import deque, defaultdict
def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    q = deque([destination])
    visit = [-1 for _ in range(n+1)]
    visit[destination] = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visit[i] == -1:
                visit[i] = visit[node] + 1
                q.append(i)
    
    return [visit[j] for j in sources]
