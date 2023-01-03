# import module
from collections import deque

# input
r, c = map(int, input().split())
rooms = []
for i in range(r):
    rooms.append(list(map(int, input().split())))

# value
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
password = [0, 0]


# BFS
def bfs(q):
    last_cnt = 0
    last_num = 0
    while q:
        one, two, cnt = q.popleft()
        if cnt == 3:
            visit[m][n] = 0

        if cnt > last_cnt:
            last_cnt = cnt
            last_num = rooms[one][two]
        elif cnt == last_cnt and last_num < rooms[one][two]:
            last_num = rooms[one][two]

        for j in range(4):
            x = one + dx[j]
            y = two + dy[j]
            if 0 <= x < r and 0 <= y < c:
                if rooms[x][y] > 0 and visit[x][y] == 0:
                    visit[x][y] = visit[one][two] + 1
                    q.append([x, y, cnt+1])

    return [last_num, last_cnt]


for m in range(r):
    for n in range(c):
        if rooms[m][n] > 0:
            visit = [[0]*c for _ in range(r)]
            visit[m][n] = 1
            Q = deque([[m, n, 1]])
            result = bfs(Q)
            result[0] += rooms[m][n]
            if password[1] < result[1]:
                password = result
            elif password[1] == result[1] and password[0] < result[0]:
                password = result

print(password[0])
