import sys
sys.setrecursionlimit(10**6)

n = int(input())
rgb_graph = []
for _ in range(n):
    rgb_graph.append([color for color in input()])

import copy
rb_graph = copy.deepcopy(rgb_graph)

for i in range(n):
    for j in range(n):
        if rb_graph[i][j] == 'G':
            rb_graph[i][j] = 'R'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def rgb(x, y, graph):
    
    rgb_color = graph[x][y]
    graph[x][y] = 0 # visit
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] != 0:
                if graph[nx][ny] == rgb_color:
                    rgb(nx, ny, graph)

                    
rgb_cnt, rb_cnt = 0, 0
for i in range(n):
    for j in range(n):
        if rgb_graph[i][j] != 0:
            rgb(i, j, rgb_graph)
            rgb_cnt += 1
        
        if rb_graph[i][j] != 0:
            rgb(i, j, rb_graph)
            rb_cnt += 1

print(rgb_cnt, rb_cnt)