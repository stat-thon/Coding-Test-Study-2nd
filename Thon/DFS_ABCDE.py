import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

from collections import defaultdict

graph = defaultdict(list)

for _ in range(m):
    r0, r1 = map(int, input().split())
    graph[r0].append(r1)
    graph[r1].append(r0)
    
# define dfs
def dfs(x, level, visited):
    if level == 4:
        print(1)
        sys.exit()
    
    for p in graph[x]:
        if visited[p] == 0:
            visited[p] = 1
            dfs(p, level + 1, visited)
            visited[p] = 0
            
for x in range(n):
    visited = [0] * n
    visited[x] = 1    
    dfs(x, 0, visited)
        
print(0)
