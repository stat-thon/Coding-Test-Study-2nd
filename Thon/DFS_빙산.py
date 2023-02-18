
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

iceberg = []

for _ in range(n):
    iceberg.append(list(map(int, input().split())))

# bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_melt(x, y):
    sea = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if iceberg[nx][ny] == 0:
            sea += 1
    
    melt.append((x, y, sea))


def bfs(x, y):

    global whole_melt
    dq = deque()
    dq.append((x, y))

    while dq:
        qx, qy = dq.popleft()
        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and iceberg[nx][ny] != 0:
                visited[nx][ny] = 1
                whole_melt -= 1
                dq.append((nx, ny))

year = 0
while True:

    melt = []
    whole_melt = 0
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                count_melt(i, j)
                whole_melt += 1
    
    if whole_melt == 0:
        year = 0
        break

    visited = [[0] * m for _ in range(n)]
    bfs(melt[0][0], melt[0][1])
    
    if whole_melt != 0:
        break

    while melt:
        qx, qy, sea = melt.pop()
        iceberg[qx][qy] = max(0, iceberg[qx][qy] - sea)
    
    year += 1

print(year)