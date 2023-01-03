import sys
sys.setrecursionlimit(100000)


n,m=list(map(int,input().split()))
arr=[]
for i in range(n):
  arr.append(list(map(int,input().split())))


dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
count=0


def dfs(x,y) :
  arr[x][y]=0
  for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<= nx < n and 0 <= ny < m and arr[nx][ny]==1:
      dfs(nx,ny)


for i in range(n):
  for j in range(m):
    if arr[i][j]==1 :
      dfs(i,j)
      count +=1


print(count)
