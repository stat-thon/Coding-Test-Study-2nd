from collections import deque 
def bfs(x,y,maps,n,m):
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q=deque()
    q.append((x,y))
    
    while q :
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]== 1:
                q.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1
    return maps[n-1][m-1]
    
            
def solution(maps):
    m=len(maps[0])
    n=len(maps)
    if bfs(0,0,maps,n,m) == 1 :
        return -1
    else: 
        return bfs(0,0,maps,n,m)
