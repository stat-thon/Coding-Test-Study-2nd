from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    board = [[0]*200 for _ in range(200)]
    
    for r in rectangle:
        for x in range(r[0]*2,r[2]*2+1):
            for y in range(r[1]*2,r[3]*2+1):
                board[y][x]=1
                
    for r in rectangle:
        for x in range(r[0]*2+1,r[2]*2):
            for y in range(r[1]*2+1,r[3]*2):
                board[y][x]=0
    

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    
    
    def bfs(x,y):
        queue = deque()
        cnt=0
        queue.append((x,y,cnt))
        visited[x][y]=1
        
        while queue:
            x,y, cnt = queue.popleft()
            if x==itemY*2 and y==itemX*2:
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if board[nx][ny]==1:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        queue.append((nx,ny,cnt+1))
        return cnt
    visited=[[0]*200 for _ in range(200)]
    cnt = bfs(characterY*2,characterX*2)

    return cnt//2
