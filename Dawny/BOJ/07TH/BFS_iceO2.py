# module
import sys
from collections import deque
input2 = sys.stdin.readline

# input
n, m = map(int, input2().split())
iceberg = []
for _ in range(n):
    iceberg.append(list(map(int, input2().split())))


def bfs(start, end):
    visit[start][end] = 1
    q = deque([[start, end]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        a, b = q.popleft()
        cnt = 0
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < n and 0 <= y < m:
                if visit[x][y] == 0:
                    if iceberg[x][y] != 0:
                        visit[x][y] = 1
                        q.append([x, y])
                    else:
                        cnt += 1
        iceberg[a][b] -= min(cnt, iceberg[a][b])


year = 0
while True:
    d = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if iceberg[j][k] != 0 and visit[j][k] == 0:
                d += 1
                bfs(j, k)

    if d == 0:
        print(0)
        break
    elif d > 1:
        print(year)
        break
    year += 1
