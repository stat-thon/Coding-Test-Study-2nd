n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([i for i in input()])

def dfs1(x, y):

    if y < 0 or y >= m:
        return

    if graph[x][y] == '|':
        return

    if visited[x][y] == 0:
        if graph[x][y] == '-':
            visited[x][y] = 1

            dfs1(x, y - 1)
            dfs1(x, y + 1)

        return 
    
    return

def dfs2(x, y):

    if x < 0 or x >= n:
        return

    if graph[x][y] == '-':
        return

    if visited[x][y] == 0:
        if graph[x][y] == '|':
            visited[x][y] = 1

            dfs2(x - 1, y)
            dfs2(x + 1, y)

        return 
    
    return


visited = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            cnt += 1            
            if graph[i][j] == '-':
                dfs1(i, j)
            else:
                dfs2(i, j)
print(cnt)