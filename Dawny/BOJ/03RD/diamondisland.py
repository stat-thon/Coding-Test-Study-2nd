# module
import sys
from collections import deque

# input
input2 = sys.stdin.readline
r, c = map(int, input().split(' '))
island = []
for i in range(r):
    island.append(list(input2().strip()))

# value
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# BFS
def bfs(a, b):
    cnt = 0
    q = deque([[a, b, cnt]])
    visit[a][b] = 1
    while q:
        m, n, cnt = q.popleft()
        for z in range(4):
            x = dx[z] + m
            y = dy[z] + n
            if 0 <= x < r and 0 <= y < c:
                if island[x][y] == "L" and visit[x][y] == 0:
                    q.append([x, y, cnt+1])
                    visit[x][y] = 1

    return cnt


# run this algorithm
distance = 0
for j in range(r):
    for k in range(c):
        if island[j][k] == "L":
            visit = [[0]*c for _ in range(r)]
            tmp = bfs(j, k)
            distance = max(distance, tmp)
print(distance)
