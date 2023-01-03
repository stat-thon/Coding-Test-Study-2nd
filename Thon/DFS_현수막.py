# Input
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([int(i) for i in input().split()])

# Set 8 directions
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [0, 1, -1, 0, 1, -1, 1, -1]

# Visit
visited = [[0] * m for _ in range(n)]

# Use dfs to spread out and check whole graph
def dfs(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    if visited[x][y] == 1:
        return 0
    
    visited[x][y] = 1

    if graph[x][y] == 1:
        
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            dfs(nx, ny)
    
        return 1
    
    return 0

# Count How many 1's returned
cnt = 0
for i in range(n):
    for j in range(m):
        cnt += dfs(i, j)

print(cnt)