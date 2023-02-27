def solution(board, moves):
    answer = 0
    basket =[0]
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1]!=0:
                if basket[-1]!=board[j][i-1]:
                    basket.append(board[j][i-1])
                    board[j][i-1] =0
                else:
                    basket.pop(-1)
                    board[j][i-1] =0
                    answer+=1
                break
    return answer*2
