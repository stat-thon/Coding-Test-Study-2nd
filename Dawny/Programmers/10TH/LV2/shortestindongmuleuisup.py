from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque([[0, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        a, b = q.popleft()
        if a == n-1 and b == m-1:
            return maps[a][b]
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < n and 0 <= y < m and maps[x][y] == 1:
                maps[x][y] = maps[a][b] + 1
                q.append([x, y])
    return -1
