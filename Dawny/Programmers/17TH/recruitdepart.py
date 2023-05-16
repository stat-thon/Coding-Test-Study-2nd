from collections import deque
def solution(scores):
    rank = 1
    wanho = scores[0]
    s = sorted(scores, key = lambda x: (-x[0], x[1]))
    q = deque(s)
    q2 = deque([[0, 0]])
    
    while q:
        a = q.popleft()
        if q2[-1][0] == a[0] or a[1] >= q2[-1][1]:
            q2.append(a)
    q2.popleft()
    
    while q2:
        rival = q2.popleft()
        if wanho[0] < rival[0] and wanho[1] < rival[1]:
            return -1
        
        if sum(wanho) < sum(rival):
            rank += 1
        
    return rank
