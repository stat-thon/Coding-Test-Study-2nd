def solution(board):
    # count O, X
    count_O, count_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                count_O += 1
            elif board[i][j] == 'X':
                count_X += 1
    
    # O보다 X가 더 많으면 무조건 틀림
    if count_O < count_X:
        return 0
    
    if count_O > count_X + 1:
        return 0
    
    # 승리 상황임에도 게임이 더 진행된 경우
    
    for i in range(3):
        # 가로줄 승리
        if board[i] == 'OOO' and count_O == count_X:
            return 0
        elif board[i] == 'XXX' and count_O > count_X:
            return 0
        # 세로줄 승리
        
        elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O' and count_O == count_X:
            return 0
        elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X' and count_O > count_X:
            return 0
        
    # 대각선 승리
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' and count_O == count_X:
        return 0
    
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' and count_O == count_X:
        return 0
    
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' and count_O > count_X:
        return 0
    
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' and count_O > count_X:
        return 0
    
    return 1