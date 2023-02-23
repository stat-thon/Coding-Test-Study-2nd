from collections import deque
def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    maps2 = list(map(list, maps))
    
    def bfs(r, c):
        cnt = int(maps2[r][c])
        q = deque([[r, c]])
        maps2[r][c] = "X"
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while q:
            a, b = q.popleft()
            for i in range(4):
                x = dx[i] + a
                y = dy[i] + b
                if 0 <= x < n and 0 <= y < m and maps2[x][y] != "X":
                    cnt += int(maps2[x][y])
                    maps2[x][y] = "X"
                    q.append([x, y])
                    
        return cnt
    
    island = [-1]
    for j in range(n):
        for k in range(m):
            if maps2[j][k] != "X":
                island.append(bfs(j, k))
                
    return island[:1] if len(island) == 1 else sorted(island[1:])
