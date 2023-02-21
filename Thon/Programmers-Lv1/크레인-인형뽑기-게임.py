from collections import deque

def solution(board, moves):
    board_transpose = []
    for i in range(len(board[0])):
        temp_list = []
        for j in range(len(board)):
            temp_list.append(board[j][i])
        board_transpose.append(temp_list)
    
    picked_doll = []
    result = 0
    for move in moves:    
        if sum(board_transpose[move - 1]) != 0:
            for idx, doll in enumerate(board_transpose[move - 1]):
                if doll != 0:
                    board_transpose[move - 1][idx] = 0
                    if len(picked_doll) != 0 and picked_doll[-1] == doll:
                        result += 2
                        picked_doll = picked_doll[:-1]
                    else:
                        picked_doll.append(doll)
                    break
                    
    return result