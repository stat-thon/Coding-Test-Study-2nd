# module
from itertools import combinations
from collections import deque
import sys
input2 = sys.stdin.readline

# input
student = [input2() for _ in range(5)]

# value
positions = [[i, j] for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
ans = 0


# bfs
def bfs(s):
    visit = [0] * 25
    l = 1
    if student[s[0][0]][s[0][1]] == "S":
        cnt = 1
    else:
        cnt = 0
    q = deque([s[0]])
    visit[5*s[0][0] + s[0][1]] = 1

    while q:
        a, b = q.popleft()
        if l - cnt > 3:
            return 0
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if [x, y] in s and visit[5 * x + y] == 0:
                visit[5 * x + y] = 1
                l += 1
                if student[x][y] == "S":
                    q.append([x, y])
                    cnt += 1
                else:
                    q.append([x, y])
    return 0 if (cnt < 4) or (sum(visit) != 7) else 1


# iter
for c in combs:
    if bfs(c) == 1:
        ans += 1
print(ans)
