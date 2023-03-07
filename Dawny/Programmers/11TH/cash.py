from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cash = deque(["0"] * cacheSize)
    q = deque(cities)
    playtime = 0
    while q:
        dosi = q.popleft()
        if dosi.lower() in cash:
            playtime += 1
            cash.remove(dosi.lower())
            cash.appendleft(dosi.lower())
        else:
            playtime += 5
            cash.pop()
            cash.appendleft(dosi.lower())

    return playtime
