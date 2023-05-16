# input
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append([s for s in input()])

# bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
dq = deque() # start_x, start_y, dist
dq.append((0, 0, 1))

while dq:
    x, y, dist = dq.popleft()
    
    if x == n - 1 and y == m - 1:
        break
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1':
            dq.append((nx, ny, dist + 1))
            graph[nx][ny] = '0'

print(dist)