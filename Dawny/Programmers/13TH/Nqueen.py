def dfs(queen, n, row):
    cnt = 0
    
    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col

        for x in range(row):
            
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]: 
                break
                
            # 대각선으로 겹치면 안됨
            if abs(queen[x]-queen[row]) == (row-x):
                break
                
        else:
            cnt += dfs(queen, n, row+1)
        
    return cnt

def solution(n):
    if 1 < n < 4:
        return 0
    elif n == 1:
        return 1
    queen = [0] * n
    return dfs(queen, n, 0)
