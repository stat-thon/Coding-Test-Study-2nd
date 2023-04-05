from collections import defaultdict, deque
def solution(tickets):
    도착경로 = deque([])
    
    항로 = defaultdict(list)
    for i, j in tickets:
        항로[i].append(j)
    
    for k in 항로.keys():
        항로[k].sort(reverse = True)
    
    stack = ['ICN']
    while stack:
        dosi = stack.pop()
        
        if dosi not in 항로 or not 항로[dosi]:
            도착경로.appendleft(dosi)
            
        else:
            stack.append(dosi)
            stack.append(항로[dosi].pop())
    
    return list(도착경로)
