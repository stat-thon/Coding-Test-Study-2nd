# 두 가지 방법
def solution(m, n, puddles):
    maps = [[1 for _ in range(m)]] + [[1] + [-1 for _ in range(m-1)] for _ in range(n-1)]
    for i, j in puddles:
        maps[j-1][i-1] = 0
    
    for i in range(1, n):
        if maps[i][0] == 0:
            for k in range(i, n):
                maps[k][0] = 0
            break
    
    for j in range(1, m):
        if maps[0][j] == 0:
            for k in range(j, m):
                maps[0][k] = 0
            break
                
    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] == -1:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
    
    
    return maps[n-1][m-1] % 1000000007 if maps[n-1][m-1] != -1 else 0
  
  def solution(m, n, puddles):
    maps = [[0 for _ in range(m+1)]] + [[0] + [-1 for _ in range(m)] for _ in range(n)] 
    
    maps[1][1] = 1
    for i, j in puddles:
        maps[j][i] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] == -1:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
    
    return maps[n][m] % 1000000007 if maps[n][m] != -1 else 0
