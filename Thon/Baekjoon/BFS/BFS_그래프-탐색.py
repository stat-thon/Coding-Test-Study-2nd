# input n, m
n, m = map(int, input().split())

# graph
from collections import defaultdict
graph = defaultdict(dict)

for _ in range(m):
    city1, city2 = map(int, input().split())
    graph[city1][city2] = 1
    graph[city2][city1] = 1
    
# bfs
from collections import deque

def bfs(graph):
    result = [-1] * n
    result[0] = 0
    
    dq = deque()
    dq.append((1, 0))
    
    while dq:
        city, cnt = dq.popleft()
        
        for next_city in graph[city].keys():
            if result[next_city - 1] == -1: # not visited
                result[next_city - 1] = cnt + 1
                dq.append((next_city, cnt + 1))
    
    return result

# input q and print output
q = int(input())

for _ in range(q):
    status, city1, city2 = map(int, input().split())
    if status == 1: # connect bridge
        graph[city1][city2] = 1
        graph[city2][city1] = 1
        
    else:
        del graph[city1][city2]
        del graph[city2][city1]

    result = bfs(graph)
    print(*result)