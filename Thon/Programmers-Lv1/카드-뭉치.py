from collections import deque

def solution(cards1, cards2, goal):
    
    make = []
    card1, card2, dq = deque(cards1), deque(cards2), deque(goal)
    
    while dq:
        q = dq.popleft()
        
        if card1:
            if card1[0] == q:
                card1.popleft()
                continue
        
        if card2:
            if card2[0] == q:
                card2.popleft()
                continue
        
        return "No"
        
    return "Yes"