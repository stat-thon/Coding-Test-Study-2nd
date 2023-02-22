import heapq

def solution(k, score):
    hof = []
    result = []
    for s in score:
        if len(hof) < k:
            heapq.heappush(hof, s)
        else:
            heapq.heappush(hof, s)
            heapq.heappop(hof)
            
        result.append(min(hof))
            
    return result