from collections import deque
import sys
input = sys.stdin.readline
t = int(input())


def distance(x1,y1,x2,y2):
    dis = abs(x1-x2) + abs(y1-y2)
    return dis

def bfs(x,y):
    
    queue = deque()
    
    queue.append((x,y))
    visited=set()
    visited.add((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        if distance(x,y,f_x,f_y)<=1000:
            return True
        
        for i in range(n):
            c_x , c_y= c_xy[i]
            if (c_x,c_y) not in visited:
                if distance(x,y, c_x,c_y)<=1000:
                    visited.add((c_x,c_y))
                    queue.append((c_x,c_y))
    return False
    

for _ in range(t):
    n = int(input())
    
    h_x , h_y = map(int,input().split())
    c_xy = [list(map(int,input().split())) for _ in range(n)]
    f_x , f_y = map(int,input().split())
    
    if bfs(h_x,h_y)==True:
        print("happy")
    else:
        print("sad")
