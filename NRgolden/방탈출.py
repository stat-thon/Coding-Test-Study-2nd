from collections import deque




n , m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]



dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    
    global MAX
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        
        x , y = queue.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0<=nx < n and 0<=ny < m):
                
                if graph[nx][ny]==0:
                    continue
                if graph[nx][ny]!=0 and visited[nx][ny]==0 :
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx,ny))
     
  
    MAX = visited[x][y]
    end_pw = graph[x][y]

                
    return MAX, end_pw
final_max = -9999
pw = -9999
# pw_dict = {}
for i in range(n):
    for j in range(m):
        MAX = -99999
        visited = [[0]*m for _ in range(n)]
        if graph[i][j]!=0:
            MAX_, end_pw  = bfs(i,j)
            if (final_max < MAX_):
                final_max = MAX_
                pw = end_pw+graph[i][j]
            elif (final_max == MAX_):
                if pw < end_pw+graph[i][j]:
                    pw = end_pw+graph[i][j]

if final_max==-9999:
    print(0)
print(pw)
