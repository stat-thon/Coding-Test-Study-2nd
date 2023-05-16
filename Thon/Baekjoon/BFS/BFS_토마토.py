import sys
m, n, h = map(int, sys.stdin.readline().split())

graph = []
for _ in range(h):
    co = []
    for _ in range(n):
        co.append(list(map(int, sys.stdin.readline().split())))
    graph.append(co)
    
# prepare for bfs
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# find points
from collections import deque
dq = deque()
num_space = h * n * m
num_nothing = 0
num_grown = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            
            # 익은 토마토
            if graph[z][y][x] == 1:
                num_grown += 1
                dq.append((x, y, z, 0))
                
            # 아무것도 없는 곳
            elif graph[z][y][x] == -1:
                num_nothing += 1

# bfs
def bfs(dq):

    global num_grown
    
    while dq:
    
        x, y, z, day = dq.popleft()
    
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
        
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                num_grown += 1
                dq.append((nx, ny, nz, day + 1))
    
    # return            
    if num_nothing + num_grown != num_space:
        return -1
    else:
        return day

if num_nothing + num_grown == num_space:
    print(0)
else:
    print(bfs(dq))