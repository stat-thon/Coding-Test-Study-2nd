from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if arr[nx][ny] >= 1:
                    arr[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
count = 0
while 1:
    visited = [[0]*m for _ in range(n)]
    bfs()
    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                c = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if c == 1:
        count += 1
    else:
        break

print(count)
  
  
    

  
