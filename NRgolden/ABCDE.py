n, m = map(int,input().split())

graph =[[] for _ in range(n)]
for i in range(m):
    a , b = map(int,input().split()) 
    
    graph[a].append(b)
    graph[b].append(a)

    
    
import sys




def dfs(L,depth):
    
    if depth >= 4:
        print(1)
        sys.exit(0)
    

    visited[L]=1


    for i in graph[L]:
        if visited[i]==0:
            visited[i]=1
            dfs(i,depth+1)
            visited[i]=0
            
for i in range(n):
    visited= [0]*n
    dfs(i,0)
    
    
print(0)
