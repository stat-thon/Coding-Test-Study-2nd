from collections import deque
def solution(board):
    n = len(board)
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    def bfs(x, y, cost, d):
        graph = [[0]*n for _ in range(n)]
        q = deque([[x, y, cost, d]])
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    graph[i][j] = -1

        while q:
            a, b, cost, before = q.popleft()
            if a == b == n-1:
                continue

            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0 <= x < n and 0 <= y < n and graph[x][y] != -1:
                    if k == before:
                        newcost = cost + 1
                    else:
                        newcost = cost + 6

                    if graph[x][y] == 0 or graph[x][y] > newcost:
                        graph[x][y] = newcost
                        q.append([x, y, newcost, k])
                        
        return graph[n-1][n-1]
    
    return min(bfs(0, 0, 0, 0), bfs(0, 0, 0, 1)) * 100
 
##### 전현서 ####
from collections import deque

def solution(board):
    result = 10000
    N = len(board)
    direction = [[0, 1, 0], [1, 0, 1], [0, -1, 2], [-1, 0, 3]]
    dp = [[[10000] * N for i in range(N)] for j in range(4)]
    queue = deque()
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    while queue:
        x, y, m, d = queue.popleft()
        for i in range(4):
            new_x = x + direction[i][0]
            new_y = y + direction[i][1]
            if -1 < new_x < N and -1 < new_y < N and board[new_x][new_y] == 0:
                new_m = m + 1
                if not d == direction[i][2]:
                    new_m += 5
                if new_m < dp[direction[i][2]][new_x][new_y]:
                    dp[direction[i][2]][new_x][new_y] = new_m
                    if new_x == N-1 and new_y == N-1:
                        continue
                    queue.append([new_x, new_y, new_m, direction[i][2]])
    for i in range(4):
        result = min([result, dp[i][N-1][N-1]])
    return result * 100
