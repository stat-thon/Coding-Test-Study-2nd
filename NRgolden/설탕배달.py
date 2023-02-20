from collections import deque

n = int(input())

sugar = [5,3]

def bfs(s):
    queue = deque()
    cnt = 0
    queue.append((s, cnt))
    visited=set()
    visited.add(s)
    
    while queue:
        s, cnt= queue.popleft()
        
        if s==0:
            return cnt
        
        for i in range(2):
            ns = s - sugar[i]
            if ns>=0:
                if ns not in visited:
                    visited.add(ns)
                    queue.append((ns,cnt+1))
                    
    return -1 
print(bfs(n))
