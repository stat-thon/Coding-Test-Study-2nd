from collections import deque

def solution(m, musicinfos):
    qq = deque(m)
    cri = []
    trac = []
    while qq:
        aa = qq.popleft()
        if qq and qq[0] == "#":
            cri.append(aa + qq.popleft())
        else:
            cri.append(aa)  
    
    info = list(map(lambda x: x.replace(':', ',').split(','), musicinfos))
    for setting in info:
        l = (int(setting[2]) - int(setting[0]))*60 + (int(setting[3]) - int(setting[1]))
        q = deque(setting[5])
        eum = []
        while q:
            a = q.popleft()
            if q and q[0] == "#":
                eum.append(a + q.popleft())
            else:
                eum.append(a)
        
        p, r = divmod(l, len(eum))
        song = deque(eum * p + eum[:r])
        maxcnt = 0
        while song:
            cnt = 0
            point = song.popleft()
            if point == cri[0]:
                cnt += 1
                for i in cri[1:]:
                    if song and song[0] == i:
                        song.popleft()
                        cnt += 1
                    else:
                        break
            maxcnt = max(maxcnt, cnt)
        if len(cri) == maxcnt:
            trac.append([setting[4], l])

    answer = sorted(trac, key = lambda x: -x[1])
    return answer[0][0] if answer else "(None)"
