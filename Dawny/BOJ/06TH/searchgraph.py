# module
from collections import defaultdict, deque

# input
n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

repair = int(input())


def bfs(start):
    q = deque([start])
    visit = [-1] * (n + 1)
    visit[start] = 0
    while q:
        st = q.popleft()
        for i in graph[st]:
            if visit[i] == -1:
                visit[i] = visit[st] + 1
                q.append(i)
    return visit[1:]


for _ in range(repair):
    op, s, e = map(int, input().split())
    if op == 1:
        graph[s] += [e]
        graph[e] += [s]
    else:
        graph[s].remove(e)
        graph[e].remove(s)
    num = bfs(1)
    print(*num)
