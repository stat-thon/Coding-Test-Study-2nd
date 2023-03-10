from collections import deque
def solution(cacheSize, cities):
    time = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            
            cache.remove(city)
            time += 1
            cache.append(city)
            
        else:
            
            if len(cache) >= cacheSize:
                
                cache.popleft()
            
            time += 5
            cache.append(city)
            
    return time