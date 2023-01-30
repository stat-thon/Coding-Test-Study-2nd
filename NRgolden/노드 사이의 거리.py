from collections import deque, defaultdict


n , m = map(int,input().split())
# graph=[[0]*n for _ in range(n)]
graph = defaultdict(dict)
for i in range(n-1):
    a,b,d = map(int,input().split())
    
    graph[a-1][b-1]=d
    graph[b-1][a-1]=d
    
    
q=[]
for j in range(m):
    a,b = map(int,input().split())
    
    q.append(b-1)

def bfs(s,e):
    
    queue = deque()
    d = 0
    queue.append((s,d))
    visited[s]=1
    
    while queue:
        
        s ,d = queue.popleft()
        
        if s==e:
            break
        
    
        for k,v in graph[s].items():
            if visited[k]==0:
                queue.append((k, d+v))
                visited[k]=1
    return d            

for k,j in q.items():
    visited=[0]*n
    distance = bfs(k,j)
    print(distance, end=' ')
