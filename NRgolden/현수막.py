from collections import deque
# import sys


# sys.setrecursionlimit(10**6)
# m , n = map(int,input().split())


# graph = []
# for i in range(m):
#     graph.append(list(map(int,input().split())))

def bfs(x,y):
    
    queue=deque()
    graph[x][y]=0
    queue.append((x,y))
    
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(8):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or ny <0 or nx >=m or ny >=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                
                
result=0   
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
            result+=1
