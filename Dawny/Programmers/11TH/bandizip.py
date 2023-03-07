from collections import deque

def solution(msg):
    dic = {chr(b):a for a, b in enumerate(range(65,91), start = 1)}
    dic[''] = 0
    n = ''
    q = deque(msg + "-")
    end = 26
    r = []
    
    while q:
        n = n[-1] if n else ''
        while q and n in dic:
            a = q.popleft()
            n += a
        end += 1
        r.append(dic[n[:-1]])
        dic.setdefault(n, end)
    
    return r
            
