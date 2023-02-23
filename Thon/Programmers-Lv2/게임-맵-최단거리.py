from collections import deque
def solution(maps):
    
    def bfs(x, y):
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        dq = deque()
        dq.append((x, y, 1))
        maps[x][y] = 0
        m, n = len(maps), len(maps[0])
        
        while dq:
            qx, qy, dist = dq.popleft()
            
            if qx == m - 1 and qy == n - 1:
                break
            
            for d in range(4):
                nx = qx + dx[d]
                ny = qy + dy[d]
                
                if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    dq.append((nx, ny, dist + 1))
        
        if qx != m - 1 or qy != n - 1:
            return -1
        
        return dist

    return bfs(0, 0)
