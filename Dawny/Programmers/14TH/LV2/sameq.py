from collections import deque
def solution(queue1, queue2):
    
    if sum(queue1) + sum(queue2) % 2 == 1:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    s1 = sum(q1)
    s2 = sum(q2)
    while cnt < (len(queue1)*3):
        
        if s1 == s2:
            return cnt
        
        elif s1 > s2:
            out = q1.popleft()
            q2.append(out)
            s1 -= out
            s2 += out
        
        else:
            out = q2.popleft()
            q1.append(out)
            s1 += out
            s2 -= out
            
        cnt += 1
            
    return -1
