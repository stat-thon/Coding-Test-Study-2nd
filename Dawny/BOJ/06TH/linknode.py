# module
from collections import deque, defaultdict

# input
n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

# value
visit = [0] * (n+1)
cnt = 0


def bfs(start):
    q = deque([[start, 0]])
    while q:
        s, c = q.popleft()
        for i in graph[s]:
            if visit[i] == 0:
                visit[i] = 1
                q.append([i, c])


for j in range(1, n+1):
    if visit[j] == 0:
        visit[j] = 1
        bfs(j)
        cnt += 1

print(cnt)
