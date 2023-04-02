from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    mapsize = 103
    maps = [[-1 for _ in range(mapsize)] for _ in range(mapsize)]
    for sx, sy, ex, ey in rectangle:
        for i in range(sx * 2, ex * 2 + 1):
            for j in range(sy * 2, ey * 2 + 1):
                maps[i][j] = 0
                
    for sx, sy, ex, ey in rectangle:    
        for i in range(sx  * 2 + 1, ex * 2):
            for j in range(sy * 2 + 1, ey * 2):
                maps[i][j] = -1
    
    q = deque([[characterX * 2, characterY * 2]])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        a, b = q.popleft()
        if [a, b] == [itemX * 2, itemY * 2]:
            return maps[a][b]//2
            
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < mapsize and 0 <= y < mapsize and maps[x][y] == 0:
                q.append([x, y])
                maps[x][y] = maps[a][b] + 1
