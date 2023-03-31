### 내 풀이
'''
내부 좌표를 집합으로 저장해서 차집합 구하면 된다고 생각했는데 이 경우 가로질러서 갈 수 있는 경로가 있어서 문제였음.
'''
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    bound = set()
    inner = set()
    for lx, ly, rx, ry in rectangle:
        w, h = rx - lx, ry - ly
        
        # 외곽 좌표 bound로 추가
        for i in range(h + 1):
            bound.add((lx, ly + i))
            bound.add((rx, ly + i))
        
        for j in range(1, w):
            bound.add((lx + j, ly))
            bound.add((lx + j, ry))
        
        # 내부 좌표 inner로 추가
        for i in range(1, h):
            for j in range(1, w):
                inner.add((lx + j, ly + i))
    
    # 가능 영역
    moves = bound - inner
    
    # bfs
    from collections import deque
    dq = deque()
    dq.append((characterX, characterY, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = set()
    
    while dq:
        
        qx, qy, cnt = dq.popleft()
        
        if qx == itemX and qy == itemY:
            return cnt
        
        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]
            
            if (nx, ny) not in visited:
                if (nx, ny) in moves:
                    visited.add((nx, ny))
                    dq.append((nx, ny, cnt + 1))
    
    return 


#####
# 답안 참고 (스케일 2배)
from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX = 0
    maxY = 0

    for x, y, x2, y2 in rectangle:
        maxX = max(x2 * 2, maxX)
        maxY = max(y2 * 2, maxY)

    graph = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    for x, y, x2, y2 in rectangle:
        for i in range((x * 2), (x2 * 2) + 1):
            for j in range((y * 2),(y2 * 2) + 1):
                graph[j][i] = 1

    for y in range(1, maxY + 1):
        for x in range(1, maxX + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    dq = deque([(cx * 2, cy * 2, 0)])
    ix *= 2
    iy *= 2
    
    while dq:
        x, y,length = dq.popleft()
        graph[y][x] = 1
        if x == ix and y == iy:
            answer = (length // 2)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                dq.append((nx, ny, length + 1))

    return answer