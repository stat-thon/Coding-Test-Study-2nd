from collections import deque
def solution(maps):
    answer = 0
    
    dx= [0,1,0,-1]
    dy= [1,0,-1,0]
    
    def bfs(x,y,dest):
        
        queue = deque()
        cnt= 0
        queue.append((x,y, cnt))
        visited[x][y]=1
        
        while queue:
            x,y, cnt= queue.popleft()
            
            if maps[x][y]==dest:
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny]!='X' and visited[nx][ny]==0:
                        visited[nx][ny]=1
                        queue.append((nx,ny,cnt+1))
                        
                        
        return x,y, cnt       
            
            
    visited=[[0]*len(maps[0]) for _ in range(len(maps))]    
        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S' and visited[i][j]==0:
                x,y ,cnt1 = bfs(i,j,'L')
                if maps[x][y]!='L':
                    return -1
                visited=[[0]*len(maps[0]) for _ in range(len(maps))]
                x1,y1,cnt2 = bfs(x,y,'E')
                if maps[x1][y1]!='E':
                    return -1
                

        
    return cnt1 + cnt2
