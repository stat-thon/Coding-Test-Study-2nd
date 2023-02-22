from collections import deque

def solution(maps):
    r, c = len(maps), len(maps[0])
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                S = [i, j]
            elif maps[i][j] == "L":
                L = [i, j]
            elif maps[i][j] == "E":
                E = [i, j]
    
    
    def bfs(X, Y):
        q = deque([X])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visit = [[0 for _ in range(c)] for _ in range(r)]
        while q:
            a, b = q.popleft()
            if [a, b] == Y:
                return visit[a][b]

            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0 <= x < r and 0 <= y < c:
                    if visit[x][y] == 0 and maps[x][y] != "X":
                        visit[x][y] = visit[a][b] + 1
                        q.append([x, y])
                
        return -1
        
    lever = bfs(S, L)
    end = bfs(L, E)
    return lever + end if lever != -1 and end != -1 else -1


        
