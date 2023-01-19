# ver1
from collections import deque

n , m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]




def bfs(x,y):
    
    
    queue = deque()
    cnt = 0
    queue.append((x,y,cnt))
    visited[x][y] = 1
    
    while queue:
        
        x, y, cnt = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx < n and 0 <= ny < m :
                if graph[nx][ny]=='L' and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny,cnt+1))

    return cnt


final_max= -99999   

for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            visited = [[0]*m for _ in range(n)]
            cnt = bfs(i,j)
            if final_max < cnt:
                final_max = cnt

print(final_max)   





# ver2
from collections import deque

n , m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]



def bfs(x,y):
    
    queue = deque()
    visited[i][j]=1
    queue.append((x,y))
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx < n and 0 <= ny < m :
                if graph[nx][ny]=='L' and visited[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                    
                    
    MAX = visited[x][y]  # 매우 중요!!!!!!!!!!
                    
    return MAX
result= -99999                
for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            visited = [[0]*m for _ in range(n)]  #매우 중요!!!!!!!!!!!
            max_ = bfs(i,j)
            
            if max_ > result:
                result = max_
            
print(result-1)      
