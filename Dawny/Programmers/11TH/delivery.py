from collections import deque
# 다익스트라
def solution(N, road, K):
    graph = {}
    for i in road:
        if i[0] in graph:
            graph[i[0]].append(i[1:])
        else:
            graph[i[0]] = [i[1:]]
        if i[1] in graph:
            graph[i[1]].append([i[0], i[2]])
        else:
            graph[i[1]] = [[i[0], i[2]]]
            
    visit = [-1] * (N+1)
    visit[1] = 0
    q = deque([[1, 0]])
    while q:
        maeul, distance = q.popleft()
        for j in graph[maeul]:
            if visit[j[0]] == -1 and K >= j[1] + distance:
                visit[j[0]] = j[1] + distance
                q.append([j[0], j[1]+distance])
                
            elif visit[j[0]] > j[1] + distance:
                visit[j[0]] = j[1] + distance
                q.append([j[0], j[1]+distance])
    
    return len(visit) - visit.count(-1)
