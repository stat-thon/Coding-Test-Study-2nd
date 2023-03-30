from collections import deque
def solution(board):
    # map
    game = [list(c) for c in board]
    
    # visit check
    visit = [[0 for _ in range(len(game[0]))] for _ in range(len(game))]
    
    # find R and G
    for i in range(len(game)):
        for j in range(len(game[0])):
            if game[i][j] == "R":
                start = [i, j]
            elif game[i][j] == "G":
                end = [i, j]
    
    # move 0u 1r 2d 3l
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    # length 
    n, m = len(game), len(game[0])
    
    # define q
    q = deque([start + [0]])
    
    # bfs
    while q:
        a, b, cnt = q.popleft()
        
        # goal
        if [a, b] == end:
            return cnt
        
        for k in range(4):
            x, y, nx, ny = a, b, dx[k], dy[k]
            
            while True:
                x += nx
                y += ny
                if 0 <= x < n and 0 <= y < m and game[x][y] == "D":
                    x -= nx
                    y -= ny
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        q.append([x, y, cnt+1])
                    break
                elif x < 0 or x == n or y < 0 or y == m:
                    x -= nx
                    y -= ny
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        q.append([x, y, cnt+1])
                    break
    return -1
