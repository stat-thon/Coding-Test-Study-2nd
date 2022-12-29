# load module
from collections import deque

# input
r, c = map(int, input().split())

# value list
cheese = []
time = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# make near cheese list
for _ in range(r):
    cheese.append(list(map(int, input().split())))

# time is answer
while 1:
    visited = [[0]*c for _ in range(r)]
    
    # BFS for external air
    Q = deque([[0, 0]])
    visited[0][0] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0:
                    if cheese[nx][ny] >= 1:
                        cheese[nx][ny] += 1
                    else:
                        visited[nx][ny] = 1
                        Q.append([nx, ny])
                        
    # check the change for cheese
    flag = 0
    for i in range(r):
        for j in range(c):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
                flag = 1
            elif cheese[i][j] == 2:
                cheese[i][j] = 1
    if flag == 1:
        time += 1
    else:
        break

print(time)

####################################
# 정답을 봤기 때문에 메모리 체크가 필요없음.
