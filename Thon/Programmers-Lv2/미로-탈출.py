from collections import deque

def solution(maps):
    
    def bfs(start_x, start_y, end_x, end_y):
    
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
    
        dq = deque()
        dq.append((start_x, start_y, 0))
    
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        visited[start_x][start_y] = 1
    
        while dq:
            qx, qy, time = dq.popleft()
        
            if qx == end_x and qy == end_y:
                return time
                break
        
            for d in range(4):
                nx = qx + dx[d]
                ny = qy + dy[d]
            
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                        visited[nx][ny] = 1
                        dq.append((nx, ny, time + 1))
    
        return 0

    # find point
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'S':
                start = (x, y)
            
            if maps[x][y] == 'E':
                end = (x, y)
                
            if maps[x][y] == 'L':
                lever = (x, y)
    
    # 시작점에서 레버 위치까지 시간
    time1 = bfs(start[0], start[1], lever[0], lever[1])
    
    # 레버 위치에서 도착점까지 시간
    time2 = bfs(lever[0], lever[1], end[0], end[1])
    
    if time1 != 0 and time2 != 0:
        return time1 + time2
    
    return -1