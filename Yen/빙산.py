import sys
from collections import deque 
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
year=0


def bfs(a,b):
  q=deque()
  q.append((a,b))
  visited[a][b]=True

  while q :
    x,y=q.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==False:
        if arr[nx][ny] != 0 :
          visited[nx][ny]=True
          q.append((nx,ny))
        else: 
          cnt[x][y]+=1
  return 0


while True :
  visited=[[False]*m for _ in range(n)]
  cnt=[[0]*m for _ in range(n)]
  a=[]

  for i in range(n):
    for j in range(m):
      if arr[i][j] !=0 and visited[i][j]==False:
        a.append(bfs(i,j))

  if len(a)==0 or len(a) >=2 :
    break

  year +=1

  for i in range(n):
    for j in range(m):
      arr[i][j] -= cnt[i][j]
      if arr[i][j] < 0 :
        arr[i][j] =0
    


if len(a) >=2 :
  print(year)
else:
  print(0)
