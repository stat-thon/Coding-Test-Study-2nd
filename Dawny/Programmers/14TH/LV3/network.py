from collections import deque
def solution(n, computers):
    cnt = 0
    visit = [0] * n
    def bfs(k):
        q = deque([k])
        while q:
            a = q.popleft()
            for j in range(n):
                if computers[a][j] == 1 and visit[j] == 0:
                    visit[j] = 1
                    q.append(j)
    
    for i in range(n):
        if visit[i] == 0:
            bfs(i)
            cnt += 1

    return cnt
