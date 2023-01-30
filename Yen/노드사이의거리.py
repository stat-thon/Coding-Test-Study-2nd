import sys
from collections import defaultdict
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
dic = defaultdict(list)

for i in range(n-1):
  a,b,d=map(int,input().split())
  dic[a].append((b,d))
  dic[b].append((a,d))



def bfs(a,b):
  q=deque()
  q.append((a,0))
  visited[a]=True
  while q :
    a,d=q.popleft()
    if a==b :
      return d 
    for i,l in dic[a]:
      if visited[i]==False :
        visited[i]=True
        q.append((i,d+l))



for i in range(m) :
  visited=[False]*(n+1)
  a,b=map(int,input().split())
  print(bfs(a,b))
