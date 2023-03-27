def solution(m, n, board):
    board = list(map(list, board))
    cnt = 0
    while True:
        visit = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if len(set(board[i][j:j+2] + board[i+1][j:j+2])) == 1 and board[i][j] != "팡!":
                    visit[i][j:j+2] = [1, 1]
                    visit[i+1][j:j+2] = [1, 1]
        
        ppopp = sum(sum(visit, []))
        if ppopp > 0:
            cnt += ppopp
            for i in range(m):
                for j in range(n):
                    if visit[i][j] == 1:
                        board[i][j] = "팡!"
            
            for i in range(m-2, -1, -1):
                for j in range(n):
                    if board[i][j] != "팡!":
                        a = 0
                        while 0 <= i+a < m-1 and board[i+1+a][j] == "팡!":
                            a += 1
                            board[i+a][j] = board[i+a-1][j]
                            board[i+a-1][j] = "팡!"
            
        else:
            break
    
    return cnt
