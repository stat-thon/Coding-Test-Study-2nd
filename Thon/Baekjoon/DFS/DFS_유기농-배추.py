# dfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # visit
                dfs(nx, ny)


# test case
import sys
sys.setrecursionlimit(10 ** 6)

t = int(input())

for _ in range(t):
    
    # input
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    # worm dfs
    worm = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                worm += 1
                dfs(i, j)
                
    print(worm)