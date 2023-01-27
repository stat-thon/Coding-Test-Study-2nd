m, n = map(int, input().split())

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

# bfs
from collections import deque
dq = deque()

# append multiple starting points
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            dq.append((i, j, 0))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(dq):
    
    while dq:
        x, y, day = dq.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = 1
                dq.append((nx, ny, day + 1))
                
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1

    return day

print(bfs(dq))