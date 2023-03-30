# 해시로 정렬해서 풀다가 완전탐색해야 한다는 걸 깨닫고 한참 헤매다가, 결국 비슷하게 해시로 푼 사람 답안 참고함.
# 불가능한 경로일 때, insert로 이전 도시를 다시 추가해주면 된다는 사실 깨달음
# 그리고 dfs로 출력한 결과를 if result로 확인하는 것 신기함.

def solution(tickets):
    
    from collections import defaultdict
    graph = defaultdict(list)
    
    for s, e in tickets:
        graph[s].append(e)
    
    for k in graph.keys():
        graph[k].sort(reverse = True)

    # dfs
    def dfs(node, path):
        
        if len(path) == len(tickets) + 1:
            return path
        
        for i, airport in enumerate(graph[node][::-1]):
            
            graph[node].pop()
            
            newpath = path[:]
            newpath.append(airport)
            
            result = dfs(airport, newpath)
            if result:
                return result
            
            graph[node].insert(i, airport)
    
    answer = dfs('ICN', ['ICN'])
    
    return answer