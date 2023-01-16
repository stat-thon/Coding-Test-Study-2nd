import sys
sys.setrecursionlimit(100000)
n=int(input())

arr=[]
for i in range(n) :
  arr.append(list(input()))

visited = [[0]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

c1=0
c2=0

def dfs(x,y) :
  visited[x][y]=1
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0 <= nx < n and 0 <= ny < n and arr[x][y]==arr[nx][ny] and visited[nx][ny]==0 :
      dfs(nx,ny)

for i in range(n):
  for j in range(n):
    if visited[i][j]==0 :
      c1 +=1
      dfs(i,j)
      
for i in range(n):
  for j in range(n):
    if arr[i][j]=="R":
      arr[i][j]="G"

visited = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if visited[i][j]==0 :
      c2 +=1
      dfs(i,j)

print(c1,c2)
