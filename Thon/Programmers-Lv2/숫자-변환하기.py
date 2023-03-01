from collections import deque

def solution(x, y, n):
    visit = set()
    dq = deque()
    dq.append((x, 0))
    
    while dq:
        q, cnt = dq.popleft()
        
        if q == y:
            break
        
        if q > y:
            continue
        
        nq = q + n
        if nq not in visit:
            visit.add(q + n)
            dq.append((q + n, cnt + 1))
            
        nq = q * 2
        if nq not in visit:
            visit.add(q * 2)
            dq.append((q * 2, cnt + 1))
        
        nq = q * 3
        if nq not in visit:
            visit.add(q * 3)
            dq.append((q * 3, cnt + 1))
    
    if q != y:
        return -1
        
    return cnt