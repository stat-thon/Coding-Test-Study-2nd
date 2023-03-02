from collections import deque
from itertools import permutations

def solution(k, dungeons):
    q = deque(permutations(dungeons, len(dungeons)))
    maxcnt = 0
    while q:
        gage = k
        d = deque(q.popleft())
        cnt = 0
        while d:
            need, tired = d.popleft()
            if gage >= need:
                gage -= tired
                cnt += 1
        maxcnt = max(maxcnt, cnt)
        print(maxcnt, cnt)
        
    return maxcnt
