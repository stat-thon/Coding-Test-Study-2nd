from collections import deque

def solution(grid):
    graph = [list(c) for c in grid]
    m = len(graph)
    n = len(graph[0])
    visit = [[[0]*4 for _ in range(n)] for _ in range(m)]
    dic = {0:[-1, 0], 1: [0, 1], 2:[1, 0], 3:[0, -1]}
    
    def bfs(a, b, c):
        q = deque([[a, b, c]])
        cnt = 0
        while q:
            x, y, z = q.popleft()
            
            if graph[x][y] == "S":
                dz = z
            elif graph[x][y] == "L":
                dz = z + 1 if z + 1 < 4 else 0
            else:
                dz = z - 1 if z - 1 > -1 else 3
            
            d = dic[dz]
            dx = x + d[0]
            dy = y + d[1]
            
            if dx == -1:
                dx = m-1
            elif dx == m:
                dx = 0
                
            if dy == -1:
                dy = n-1
            elif dy == n:
                dy = 0
                
            if visit[dx][dy][dz] == 0:
                visit[dx][dy][dz] = 1
                q.append([dx, dy, dz])
                cnt += 1
        return cnt    
            
    ans = []    
    for i in range(m):
        for j in range(n):
            for k in range(4):
                if visit[i][j][k] == 0:
                    ans.append(bfs(i, j, k))
    
    return sorted(ans)
