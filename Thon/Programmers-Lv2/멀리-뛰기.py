from collections import deque

def solution(n):
    
    if n == 1 or n == 2:
        return n
    
    dq = deque([1, 2])
    c = 2
    
    while c < n:
        c += 1
        a = dq.popleft()
        dq.append(a + dq[0])
    
    return dq[1] % 1234567