import sys
sys.setrecursionlimit(10 ** 6)

def solution(maps):
    
    # make graph
    graph = []
    
    for m in maps:
        graph.append([int(i) if i != 'X' else 0 for i in m])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # dfs
    def dfs(x, y):
        
        nonlocal cnt    
        
        cnt += graph[x][y]
        graph[x][y] = 0
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] != 0:
                    dfs(nx, ny)
        return
    
    # output    
    result = []
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if graph[x][y] != 0:
                cnt = 0
                dfs(x, y)
                result.append(cnt)
    
    if not result:
        return [-1]
    
    return sorted(result)