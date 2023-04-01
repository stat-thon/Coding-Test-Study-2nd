from itertools import permutations

def solution(k, dungeons):
    MAX = 0
    
    for dungeon in permutations(dungeons, len(dungeons)):
        newk = k
        cnt = 0
        
        for need, spend in dungeon:
            if newk >= need:
                newk -= spend
                cnt += 1
            else:
                break
            
        MAX = max(MAX, cnt)
    
    return MAX