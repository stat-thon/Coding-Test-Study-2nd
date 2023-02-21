from collections import deque

def solution(cards1, cards2, goal):
    q = deque(goal)
    c1 = deque(cards1)
    c2 = deque(cards2)
    while q:
        a = q.popleft()
        if c1 and a == c1[0]:
            c1.popleft()
        elif c2 and a == c2[0]:
            c2.popleft()
        else:
            return "No"
        
    return "Yes"
