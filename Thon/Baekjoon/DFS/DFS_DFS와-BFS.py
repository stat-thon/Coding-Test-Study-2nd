# input
n, m, start = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# dfs
import sys
sys.setrecursionlimit(10 ** 6)

result_dfs = [start]
visited = [0] * n
visited[start - 1] = 1

def dfs(x):
    
    global result_dfs
    
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            result_dfs.append(i + 1)
            dfs(i)

dfs(start - 1)
print(*result_dfs)

# bfs
from collections import deque
dq = deque()
dq.append(start - 1)

result_bfs = [start]
visited_bfs = [0] * n
visited_bfs[start - 1] = 1

while dq:
    x = dq.popleft()
    
    for i in range(n):
        if graph[x][i] == 1 and visited_bfs[i] == 0:
            visited_bfs[i] = 1
            result_bfs.append(i + 1)
            dq.append(i)

print(*result_bfs)