import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())

arr=[[] for _ in range(n+1)]

count=0

for _ in range(m):
  x,y=map(int,input().split())
  arr[x].append(y)
  arr[y].append(x)

visited=[False]*(n+1)

def dfs(x):
  visited[x]=True
  for i in arr[x]:
    if visited[i]==False :
      visited==True
      dfs(i)

for i in range(1,n+1):
  if visited[i]==False:
    dfs(i)
    count +=1


print(count)
