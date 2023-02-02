import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())

arr=[[] for _ in range(n+1)]


for _ in range(m):
  x,y=map(int,input().split())
  arr[x].append(y)
  arr[y].append(x)


def bfs(x,d) :
  l[1]=0
  q=deque()
  q.append((x,0))
  while q :
    a,b=q.popleft()
    for i in arr[a]:
      if l[i]==[] :
        q.append((i,b+1))
        l[i]=b+1


k=int(input())
for _ in range(k):
  a,i,j = map(int,input().split())
  if a==1 :
    arr[i].append(j)
    arr[j].append(i)
  else:
    arr[i].remove(j)
    arr[j].remove(i)
  l=[[] for _ in range(n+1)]
  bfs(1,0)
  for i in range(1,len(l)):
    if l[i]==[]:
      l[i]=-1
  print(*l[1:])
