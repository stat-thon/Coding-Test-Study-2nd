# 틀린 내 답
from collections import deque

def solution(cap, n, deliveries, pickups):
    dist = 0
    dlist, plist = deque(deliveries[::-1]), deque(pickups[::-1])
    
    while dlist:
        
        d = 0
        dcnt = 0
        for i in range(len(dlist)):
            d += dlist[i]
            dlist[i] = 0
            dcnt += 1
            if d > cap:
                dlist[i] += d - cap
                d = cap
                dcnt -= 1
                break
        
        p = 0
        pcnt = 0
        for i in range(len(plist)):
            p += plist[i]
            plist[i] = 0
            pcnt += 1
            if p > cap:
                plist[i] += p - cap
                p = cap
                pcnt -= 1
                break
        
        dist += len(dlist) * 2
        
        for _ in range(min(dcnt, pcnt)):
            dlist.popleft()
            plist.popleft()
        
    return dist 

############################
# 정답 풀이 - 그리디
# 그리디로 풀 때 잉여회수량, 잉여배달량이라는 개념으로 생각하여 가감 후 회복할 때까지 cap을 더한다는 아이디어를 배움
# 
# dist에 i+1을 곱하는 이유는 인덱스가 거리보다 1 작아서
def solution(cap, n, deliveries, pickups):
    dist = 0
    d, p = 0, 0
    for i in range(n - 1, -1, -1):
        
        d -= deliveries[i]
        p -= pickups[i]
        
        cnt = 0
        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1
        
        dist += (i + 1) * 2 * cnt
        
    return dist