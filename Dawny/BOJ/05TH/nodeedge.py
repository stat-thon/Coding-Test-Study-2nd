# module
from collections import deque

# input
n, m = map(int, input().split())

distance = [[0] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
question = []
q = deque([])

# graph
for i in range(n-1):
    start, end, dist = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    distance[start][end] = distance[end][start] = dist

# question
for _ in range(m):
    question.append(list(map(int, input().split())))


# dfs
def bfs(first):
    visit = [0] * (n+1)
    visit[first] = 1
    q.append([first, distance[first][first]])
    while q:
        s, d = q.popleft()
        for j in graph[s]:
            if visit[j] == 0:
                visit[j] = 1
                d += distance[s][j]
                q.append([j, d])
                if distance[first][j] == 0:
                    distance[first][j] = distance[j][first] = d
                d -= distance[s][j]


for x in range(n):
    bfs(x)

for y in question:
    print(distance[y[0]][y[1]])

