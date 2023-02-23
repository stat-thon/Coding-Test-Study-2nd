from collections import deque
def solution(n):
    
    dq = deque([0, 1])
    
    while n:
        dq.append(dq[0] + dq[1])
        dq.popleft()
        n -= 1
        
    return dq[1] % 1000000007