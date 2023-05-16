def solution(park, routes):
    
    dir = {'E':[0, 1], 'W': [0, -1], 'N': [-1, 0], 'S': [1, 0]}
    h, w = len(park[0]), len(park[1])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                start = [i, j]
    
    now = start
    for r in routes:
        d, n = r.split(' ')
        
        x, y = now
        for _ in range(int(n)):
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            
            if nx >= h or ny >= w or nx < 0 or ny < 0:
                x, y = now
                break
            else:
                if park[nx][ny] == 'X':
                    x, y = now
                    break
                else:
                    x, y = nx, ny
        
        now = [x, y]
    
    return now