import heapq

def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
    hap = sum(heap)
    
    for _ in range(n):
        if hap == 0:
            break
        hap += 1
        a = heapq.heappop(heap) + 1
        heapq.heappush(heap, a)
    
    return sum([j**2 for j in heap])
