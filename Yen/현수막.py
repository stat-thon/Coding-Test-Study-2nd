#dfs (재귀 최대 깊이 설정 필요)
#메모리: 43364KB, 시간196ms
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




# bfs 
#메모리: 34112KB, 시간160ms
from collections import deque

n,m=map(int,input().split())
arr=[]
for i in range(n):
  arr.append(list(map(int,input().split())))

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
count=0
q=deque()

def bfs(x,y) :
  q.append((x,y))
  arr[x][y]=0
  while q :
    x,y=q.popleft()
    for i in range(8) :
      nx=x+dx[i]
      ny=y+dy[i]
      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]==1 :
        q.append((nx,ny))
        arr[nx][ny]=0


for i in range(n):
  for j in range(m) :
    if arr[i][j]==1 :
      bfs(i,j)
      count +=1

print(count)

