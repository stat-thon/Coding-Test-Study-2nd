# module
import sys
import copy
from collections import deque
input2 = sys.stdin.readline

# input
n = int(input2())

# setting
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# monitor
monitor = [list(sys.stdin.readline().strip()) for i in range(n)]
monitor2 = copy.deepcopy(monitor)
for j in range(n):
    for k in range(n):
        if monitor2[j][k] == 'G':
            monitor2[j][k] = 'R'


# bfs
def bfs(j, k, color, RGB):
    Q = deque([[j, k]])
    RGB[j][k] = 'O'
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if RGB[x][y] == color:
                    Q.append([x, y])
                    RGB[x][y] = 'O'


# find
normal = 0
disease = 0
for j in range(n):
    for k in range(n):
        if monitor[j][k] != 'O':
            bfs(j, k, monitor[j][k], monitor)
            normal += 1
        if monitor2[j][k] != 'O':
            bfs(j, k, monitor2[j][k], monitor2)
            disease += 1

print(normal, disease)
