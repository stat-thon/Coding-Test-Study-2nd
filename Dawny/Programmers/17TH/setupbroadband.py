from collections import deque
def solution(n, stations, w):
    react = 2*w + 1
    already = [0]
    for i in stations:
        already.append(i-w-1)
        already.append(i+w)
    already += [n]
    q = deque(already)
    cnt = 0
    while q:
        l = q.popleft()
        r = q.popleft()
        if r - l > 0:
            a, b = divmod(r-l, react)
            cnt += a + 1 if b != 0 else a 
    return cnt
