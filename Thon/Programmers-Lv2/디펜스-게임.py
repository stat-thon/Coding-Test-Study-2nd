import heapq
from collections import deque

def solution(n, k, enemy):
    heap = []
    dq = deque(enemy)
    stage = 0
    
    while dq:
        
        q = dq.popleft()
        heapq.heappush(heap, -q)
        n -= q
        
        while n < 0 and k:
            h = -heapq.heappop(heap)
            n += h
            k -= 1
            
        if k <= 0 and n < 0:
            return stage
        
        stage += 1
        
    return stage