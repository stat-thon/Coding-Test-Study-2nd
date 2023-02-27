# 시간초과
def solution(board):
    m, n = len(board), len(board[0])
    MAX = min(m, n)
    
    # 정사각형 판별 함수
    def is_square(x, y, k):
        area = 0
        for i in range(x, x + k):
            area += sum(board[i][y: y + k])
        
        if area == k ** 2:
            return area
        return 0
    
    while MAX:
        for i in range(m - MAX + 1):
            for j in range(n - MAX + 1):
                area = is_square(i, j, MAX)
                if area != 0:
                    return area
        
        MAX -= 1
    
    
    return area