from collections import defaultdict, deque
import sys

input = sys.stdin.readline
n , m = map(int,input().split())

way = defaultdict(list)

for i in range(m):
    a, b = map(int,input().split())
    
    way[a-1].append(b-1)
    way[b-1].append(a-1)

q = int(input())

    

def bfs(s):
    
    
    queue = deque()
    cnt = 0
    queue.append((s,cnt))
    visited[s]=1
    
    while queue:
        s , cnt= queue.popleft()
        
        for i in way[s]:
            if visited[i]==0:
                visited[i]=1
                queue.append((i, cnt+1))
                dis[i]= cnt+1
            
            
for _ in range(q):
    a, i, j = map(int,input().split())
    dis =[-1]*n
    dis[0]=0
    visited=[0]*n
    if a==2:
        way[i-1].remove(j-1)
        way[j-1].remove(i-1)

    elif a==1:
        way[i-1].append(j-1)
        way[j-1].append(i-1)

    bfs(0)    
    print(*dis)
