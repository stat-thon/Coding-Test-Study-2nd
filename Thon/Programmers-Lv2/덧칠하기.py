from collections import deque
def solution(n, m, section):
    
    dq = deque(section)
    result = 0
    while dq:
        q = dq.popleft()
        
        while dq and dq[0] < q + m:
            dq.popleft()
        
        result += 1
        
    return result