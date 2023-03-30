from collections import deque

def solution(park, routes):
    # length 
    n = len(park)
    m = len(park[0])
    
    # find start point
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                place = [i, j]
                break
    
    # dic for WESN
    dic = {'N': [-1, 0], 'E':[0, 1], 'S':[1, 0], 'W':[0, -1]}
    
    # queue
    q = deque(routes)
    while q:
        change = True
        a, b = q.popleft().split(" ")
        x, y = place
        dx, dy = dic[a]
        for num in range(int(b)):
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < m and park[x][y] != "X":
                pass
            else:
                change = False
                break
        if change:
            place = [x, y]
        
    return place
