from collections import deque
import sys
input=sys.stdin.readline
n=int(input())


def bfs():
  q=deque()
  q.append((home_x,home_y))
  while q:
    x,y=q.popleft()
    if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            return 'happy'
    for i in range(m): 
      if visited[i]==False:
        new_x,new_y = graph[i] 
        if abs(x-new_x) + abs(y-new_y) <= 1000:
          visited[i] = True
          q.append((new_x,new_y)) 
  return 'sad'



for _ in range(n):
    m = int(input())
    home_x,home_y = map(int,input().split())
    graph = []
    for _ in range(m):
        x,y = map(int,input().split())
        graph.append((x,y))
    festival_x,festival_y = map(int,input().split())
    visited = [False for _ in range(m+1)]
    print(bfs())
