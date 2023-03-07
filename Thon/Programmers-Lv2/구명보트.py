from collections import deque

def solution(people, limit):
    dq = deque(sorted(people))
    boat = 0
    while dq:
        h = dq.pop()
        
        if dq and dq[0] + h <= limit:
            dq.popleft()
        
        boat += 1
            
    return boat