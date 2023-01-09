# module
import sys
from collections import deque
input2 = sys.stdin.readline

# input
n = int(input2())

# setting
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# monitor
monitor = [list(map(str, input().strip())) for i in range(n)]
visit = [[0]*n for _ in range(n)]


# bfs
def bfs(a, b):
    q = deque([[a, b]])
    visit[a][b] = 1
    while q:
        tmp = q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if monitor[x][y] == monitor[a][b] and visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append([x, y])


# find
normal = 0
for j in range(n):
    for k in range(n):
        if not visit[j][k]:
            bfs(j, k)
            normal += 1

# change this monitor
for j in range(n):
    for k in range(n):
        if monitor[j][k] == 'G':
            monitor[j][k] = 'R'

# find
disease = 0
visit = [[0]*n for _ in range(n)]
for j in range(n):
    for k in range(n):
        if not visit[j][k]:
            bfs(j, k)
            disease += 1

print(normal, disease)
