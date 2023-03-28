import heapq

def solution(operations):
    h = []
    for i in operations:
        a, b = i.split(" ")
        if a == "I":
            heapq.heappush(h, int(b))
        elif b == "-1" and h:
            heapq.heappop(h)
        elif b == "1" and h:
            h = heapq.nlargest(len(h), h)[1:]
            heapq.heapify(h)
    return [0, 0] if len(h) == 0 else [max(h), min(h)]
