from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(dict)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    
# bfs
def bfs(x):
    visit[x] = 1
    dq = deque()
    dq.append(x)
    
    while dq:
        q = dq.popleft()
        
        for node in graph[q].keys():
            if visit[node] == 0:
                visit[node] = 1
                dq.append(node)
                
    return 1

# visit
visit = [0] * (n + 1)
visit[0] = 1

# output
result = 0
for i in range(1, n + 1):
    if visit[i] == 0:
        result += bfs(i)

print(result)