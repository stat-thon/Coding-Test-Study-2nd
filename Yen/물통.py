import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())

q = deque()
q.append((0, 0))

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

# 답을 저장할 배열
answer = []




def visit(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():

    while q:
       
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        visit(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        visit(x - water, y)
        # y -> x
        water = min(y, a-x)
        visit(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        visit(x, y - water)
        # z -> x
        water = min(z, a-x)
        visit(x + water, y)
        # z -> y
        water = min(z, b-y)
        visit(x, y + water)



bfs()

answer.sort()
for i in answer:
    print(i, end=" ")
