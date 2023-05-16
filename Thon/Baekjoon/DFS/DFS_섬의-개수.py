import sys
sys.setrecursionlimit(10 ** 6)

# define dfs
dx = [-1, -1, -1, 1,  1, 1, 0,  0]
dy = [ 0,  1, -1, 0, -1, 1, 1, -1]

def dfs(x, y):
    
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

# result
while True:
    
    m, n = map(int, sys.stdin.readline().split())
    
    if n == 0 and m == 0:
        break
    
    # input
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    # dfs
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)