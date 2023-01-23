n,m=map(int,input().split())
arr=[[] for _ in range(n)]
for _ in range(m):
  x,y=map(int,input().split())
  arr[x].append(y)
  arr[y].append(x)

visited=[0]*n
result=0

def dfs(c,x):
  global result
  if c==4 :
    result =1
    return 
  for i in arr[x]:
    if visited[i]==0 :
      visited[i]=1
      dfs(c+1,i)
      visited[i]=0
    

    


for i in range(n):
  visited[i]=1
  dfs(0,i)
  visited[i]=0
  if result==1:
    break

print(result)
