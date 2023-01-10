import sys
sys.setrecursionlimit(10**6)

# input
n = int(input())
rgb_graph = []
for _ in range(n):
    rgb_graph.append([color for color in input()])

# another graph
import copy
rb_graph = copy.deepcopy(rgb_graph)

for i in range(n):
    for j in range(n):
        if rb_graph[i][j] == 'G':
            rb_graph[i][j] = 'R'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# not to be confused, i made each function using dfs for two kind of people
# first type: reg != green
def rgb(x, y):
    
    rgb_color = rgb_graph[x][y]
    rgb_graph[x][y] = 0 # visit
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < n:
            if rgb_graph[nx][ny] != 0:
                if rgb_graph[nx][ny] == rgb_color:
                    rgb(nx, ny)

# second type: red = green
def rb(x, y):
    
    rb_color = rb_graph[x][y]
    rb_graph[x][y] = 0 # visit
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < n:
            if rb_graph[nx][ny] != 0:
                if rb_graph[nx][ny] == rb_color:
                    rb(nx, ny)

# count
rgb_cnt, rb_cnt = 0, 0
for i in range(n):
    for j in range(n):
        if rgb_graph[i][j] != 0:
            rgb(i, j)
            rgb_cnt += 1
        
        if rb_graph[i][j] != 0:
            rb(i, j)
            rb_cnt += 1

print(rgb_cnt, rb_cnt)