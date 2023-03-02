def solution(cards):
    visit = list(range(1, len(cards)+1))
    score = 0
    
    def dfs(num, v):
        if visit[num-1] == 0:
            return v
        else:
            visit[num-1] = 0
            return dfs(cards[num-1], v+1)
        
    s = [0]
    for j in visit:
        if j:
            s.append(dfs(j, 0))
    go = sorted(s)
    return go[-1]*go[-2]
