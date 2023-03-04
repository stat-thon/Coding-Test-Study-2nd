from collections import deque

def bfs(maps,x,y,visit):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q=deque()
    q.append([x,y])
    
    c=0
    visit[x][y]=1
    
    while q :
        x,y=q.popleft()
        c+= int(maps[x][y])
        
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<= nx < len(maps) and 0 <= ny < len(maps[0]) :
                if visit[nx][ny]==0 and maps[nx][ny] != 'X' :
                    visit[nx][ny]=1 
                    q.append([nx,ny])
    return c

def solution(maps):
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    answer = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visit[i][j]==0 :
                a=bfs(maps,i,j,visit)
                answer.append(a)
                
    if answer :
        answer.sort()
    else:
        answer.append(-1)
    return answer
