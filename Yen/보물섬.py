from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
  arr.append(list(sys.stdin.readline().strip()))



dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j) :
  visited=[[0]*m for _ in range(n)]
  visited[i][j]=1
  q=deque()
  q.append((i,j,0))

  while q :
    x,y,c=q.popleft()
    for i in range(4):
      nx= x+dx[i]
      ny=y+dy[i]
      if 0<= nx < n and 0<= ny < m :
        if visited[nx][ny]==0 and arr[nx][ny]=='L':
          visited[nx][ny]=1
          q.append((nx,ny,c+1))
  return c


d=0
for i in range(n):
  for j in range(m):
    if arr[i][j]=='L':
      d=max(d,bfs(i,j))


print(d)
