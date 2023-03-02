from collections import deque

def solution(n, wires):
    first = wires[0]
    cnt = 101
    w = deque(wires)
    
    def bfs(w):
        maps = list(w)
        visit = [1] + [0]*(n-3)
        q = deque([maps[0]])
        while q:
            a, b = q.popleft()
            for i in range(n-2):
                if visit[i] == 0:
                    if b in maps[i]:
                        visit[i] = 1
                        q.append(maps[i])
                    elif a in maps[i]:
                        visit[i] = 1
                        q.append(maps[i])
        return sum(visit) + 1
    
    while True:
        tmp = w.popleft()
        cnt = min(cnt ,abs(2*bfs(w) - n))
        w.append(tmp)
        if w[0] == first:
            break
    
    return cnt
