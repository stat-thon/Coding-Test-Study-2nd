from collections import deque

def solution(n):
    if n % 2 == 1:
        return 0
    
    dq = deque([3, 11])
    while n > 4:
        dq.append(4 * dq[1] - dq[0])
        dq.popleft()
        n -= 2
    
    return dq[1] % 1000000007