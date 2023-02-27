from collections import deque
def solution(x, y, n):
    q = deque([y])
    visit = [0] * 1000001
    while q:
        a = q.popleft()
        if a == x:
            return visit[a]
        if a % 3 == 0 and a//3 >= x and visit[a//3] == 0:
            visit[a//3] = visit[a] + 1
            q.append(a//3)
        if a % 2 == 0 and a//2 >= x and visit[a//2] == 0:
            visit[a//2] = visit[a] + 1
            q.append(a//2)
        if a-n >= x and visit[a-n] == 0:
            visit[a-n] = visit[a] + 1
            q.append(a-n)
        
    return -1
