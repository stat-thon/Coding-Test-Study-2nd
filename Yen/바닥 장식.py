n,m=map(int,input().split())

arr=[]
visit=[[0]*m]*n
for i in range(n) :
  arr.append(list(input()))

dx=[-1,1]
dy=[-1,1]


def dfs(x,y) :
  if arr[x][y]=='-':  #'-'일때 y만 바꿔서 dfs 실행 
    arr[x][y]=1
    for i in range(2):
      ny=y+dy[i]
      if 0<= ny < m and arr[x][ny]=='-':
          dfs(x,ny)    
          
  if arr[x][y]=='|' : #'|'일때 x만 바꿔서 dfs 실행 
    arr[x][y]=1
    for i in range(2):
      nx=x+dx[i]
      if 0 <= nx < n and arr[nx][y]=='|':
          dfs(nx,y)
          
   
count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '-' or arr[i][j] == '|':
            dfs(i,j)   
            count += 1
 
print(count)   
