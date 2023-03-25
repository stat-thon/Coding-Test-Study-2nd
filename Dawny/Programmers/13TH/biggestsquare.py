def solution(board):
    n = len(board)
    m = len(board[0])
    maxnum = 0
    
    check = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for a in range(1, n+1):
        for b in range(1, m+1):
            if board[a-1][b-1] == 1:
                check[a][b] = min(check[a-1][b], check[a][b-1], check[a-1][b-1]) + 1
                if maxnum < check[a][b]:
                    maxnum = check[a][b]
                    
    print(check)
    return maxnum ** 2
