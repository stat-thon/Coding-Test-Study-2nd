from collections import deque, defaultdict
import sys

input = sys.stdin.readline
n, m = map(int,input().split())

graph= defaultdict(list)
for i in range(m):
    a, b = map(int,input().split())
    
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
def bfs(s):
    
    queue = deque()
    queue.append(s)
    visited[s]=1
    
    while queue:
        
        s = queue.popleft()
        for i in graph[s]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
                
cnt=0
visited=[0]*n
for i in range(n):
    if visited[i]==0:
        bfs(i)
        cnt+=1
print(cnt)      
