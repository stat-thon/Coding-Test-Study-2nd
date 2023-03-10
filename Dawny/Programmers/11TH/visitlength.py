from collections import deque

def solution(dirs):
    dic = {'U':[0, 1], 'D': [0, -1], 'L':[-1, 0], 'R':[1, 0]}
    visit = set()
    q = deque(dirs)
    a, b = [0, 0]
    while q:
        v = q.popleft()
        dx, dy = dic[v]
        x = dx + a
        y = dy + b
        if -5 <= x <= 5 and -5 <= y <= 5:
            visit.add((a, b, x, y))
            visit.add((x, y, a, b))
            a = x
            b = y
    return len(visit) // 2
