# input
h, w = map(int, input().split())
graph = []
for _ in range(h):
    graph.append([lw for lw in input()])

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# finding out the most far point using bfs
def bfs(x, y):
    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1
    dq = deque()
    dq.append((x, y, 0))
    
    while dq:
        qx, qy, time = dq.popleft()
        
        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]
            
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                visited[nx][ny] = 1
                dq.append((nx, ny, time + 1))
    return time

# it removes the point that cannot be the most far point
def cannot_set_treasure(tx, ty):
    if 0 < tx < h - 1:
        if graph[tx - 1][ty] == 'L' and graph[tx + 1][ty] == 'L':
            return 0
    if 0 < ty < w - 1:
        if graph[tx][ty - 1] == 'L' and graph[tx][ty + 1] == 'L':
            return 0
    return 1

# the maximum time
MAX_time = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'L' and cannot_set_treasure(i, j):
            time = bfs(i, j)
            MAX_time = max(MAX_time, time)
            
print(MAX_time)