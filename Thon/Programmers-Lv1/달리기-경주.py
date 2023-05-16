def solution(players, callings):
    
    player = {name:i for i, name in enumerate(players)}
    rank = {i:name for i, name in enumerate(players)}
    
    for name in callings:
        passed = player[name] - 1
        p_passed = rank[passed]
        rank[passed], rank[passed + 1] = name, p_passed
        
        player[name] -= 1
        player[p_passed] += 1
    
    return sorted(player, key = lambda x: player[x])