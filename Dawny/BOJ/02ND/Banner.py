# recrusion error
import sys
sys.setrecursionlimit(10**6)

# input
r, c = map(int, input().split())
banner = []
for i in range(r):
    banner.append(list(map(int, input().split())))

# value
dx = [0, 0, 1, 1, -1, 1, -1, -1]
dy = [1, -1, 1, -1, 0, 0, -1, 1]
cnt = 0


# DFS
def dfs(a, b):
    banner[a][b] = 0
    for n in range(8):
        x = a + dx[n]
        y = b + dy[n]
        if 0 <= x < r and 0 <= y < c:
            if banner[x][y] == 1:
                dfs(x, y)


# apply DFS
for j in range(r):
    for k in range(c):
        if banner[j][k] == 1:
            dfs(j, k)
            cnt += 1

print(cnt)
