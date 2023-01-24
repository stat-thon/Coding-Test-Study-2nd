n = int(input())

graph=[[] for i in range(n+1)]

for i in range(100):
    a, b = map(int,input().split())
    
    if a==-1:
        break
    
    graph[a].append(b)
    graph[b].append(a)
    
from collections import deque

def bfs(x):
    
    
    
    queue = deque()
    visited[x] = 1
    relation=0
    queue.append((x,relation))
    
    while queue:
        
        v ,relation= queue.popleft()
        
        for i in graph[v]:
            if visited[i]==0:
                visited[i] = 1
                queue.append((i,relation+1))
                
    return relation
relation_score = []



for i in range(1,n+1):
    visited =[0]*(n+1)
    r = bfs(i)
    relation_score.append(r)

relation_score.insert(0,99999)    
score_min = min(relation_score)
print(score_min, relation_score.count(score_min))
for i,j in enumerate(relation_score):
    if score_min==j:
        print(i,end=' ')
