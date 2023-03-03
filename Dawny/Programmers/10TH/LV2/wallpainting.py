from collections import deque

def solution(n, m, section):
    q = deque(section)
    cnt = 0
    while q:
        a = q.popleft()
        cnt += 1
        while q and q[0] - m < a:
            q.popleft()
            
    return cnt
