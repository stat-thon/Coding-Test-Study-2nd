# input
n, m = map(int, input().split())

from collections import defaultdict
graph = defaultdict(dict) # 해시로 시간 절약
for _ in range(n - 1):
    node0, node1, dist = map(int, input().split())
    graph[node0][node1] = dist
    graph[node1][node0] = dist

wanna_know = []
for _ in range(m):
    wanna_know.append(list(map(int, input().split())))

# bfs
from collections import deque
def bfs(start, end):
    
    visit = [0] * (n + 1)
    visit[start] = 1
    
    dq = deque()
    dq.append((start, 0))
    
    while dq:
        node_now, dist_sum = dq.popleft()
        
        # 결과 출력 조건
        if node_now == end:
            break
        
        for next_node, dist in graph[node_now].items():
            if visit[next_node] == 0:
                visit[next_node] = 1
                dq.append((next_node, dist_sum + dist))
                
    return dist_sum

# output
for output in wanna_know:
    start, end = output
    print(bfs(start, end))