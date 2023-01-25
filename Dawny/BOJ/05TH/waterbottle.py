# module
from collections import deque

# input
a, b, c = list(map(int, input().split()))
queue = deque([[0, 0, c]])

# value
case = []
visit = [[0]*(c+1) for _ in range(a+1)]
bottle = [[i for i in range(3) if i != j] for j in range(3)]


# bfs
def bfs(q):
    while q:
        x, y, z = q.popleft()
        if visit[x][z] == 0:
            visit[x][z] = 1
            if x == 0:
                case.append(z)

            q.append([min(a, x + z), y, max(x + z - a, 0)])
            q.append([max(x + z - c, 0), y, min(c, x + z)])
            q.append([x, min(b, y + z), max(y + z - b, 0)])
            q.append([x, max(y + z - c, 0), min(c, y + z)])
            q.append([min(a, x + y), max(x + y - a, 0), z])
            q.append([max(x + y - b, 0), min(b, x + y), z])


bfs(queue)
print(*sorted(case))
