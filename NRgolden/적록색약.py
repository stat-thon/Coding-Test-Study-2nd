from collections import deque
import sys


# 메모 : 34340KB 시간 : 80ms
input = sys.stdin.readline

n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph=[]
for i in range(n):
    graph.append(list(input().strip()))
    

visited = [[0]*n for _ in range(n)] 

def bfs1(x,y):
    
    queue = deque()
    
    queue.append((x,y))
    visited[x][y]=1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if graph[nx][ny]!='B':
                continue
    
            if graph[nx][ny]=='B' and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))
    
def bfs2(x,y):
    
    queue = deque()
    
    queue.append((x,y))
    visited[x][y]=1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if graph[nx][ny]!='R':
                continue
    
            if graph[nx][ny]=='R'and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))

def bfs3(x,y):
    
    queue = deque()
    
    queue.append((x,y))
    visited[x][y]=1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if graph[nx][ny]!='G':
                continue
    
            if graph[nx][ny]=='G' and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny)) 
def bfs4(x,y):
    
    queue = deque()
    
    queue.append((x,y))
    visited[x][y]=1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if graph[nx][ny]=='B':
                continue
    
            if graph[nx][ny] != 'B' and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))

                
result_b = 0    
result_r = 0
result_g = 0 
result_s = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='B' and visited[i][j]==0: 
            bfs1(i,j)
            result_b +=1
        if graph[i][j]=='G' and visited[i][j]==0:
            bfs3(i,j)
            result_g +=1
        if graph[i][j]=='R'and visited[i][j]==0:
            bfs2(i,j)
            result_r +=1      
            
visited = [[0]*n for _ in range(n)] 

for i in range(n):
    for j in range(n):
        if graph[i][j]!='B' and visited[i][j]==0:
            bfs4(i,j)
            result_s +=1       
            
print(result_b+result_r+result_g,result_b+result_s ,end=' ')
