# moduls
import sys

# input
n, m = map(int, sys.stdin.readline().split())

# friends line
line = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    line[x].append(y)
    line[y].append(x)

# value
visit = [0 for _ in range(n)]
result = 0


# dfs
def dfs(node, cnt):
    global result
    if cnt == 4:
        result = 1
        return
    for i in line[node]:
        if not visit[i]:
            visit[node] = 1
            dfs(i, cnt+1)
            visit[node] = 0


for j in range(n):
    visit[j] = 1
    dfs(j, 0)
    visit[j] = 0
    if result == 1:
        break

print(result)
