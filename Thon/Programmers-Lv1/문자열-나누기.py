from collections import deque
def solution(s):
    dq = deque([i for i in s])
    same, diff, result = 0, 0, 0
    
    temp = ''
    while len(dq) > 1:
        q = dq.popleft()
        
        if temp == '':
            temp = q
        
        if q == temp:
            same += 1
        else:
            diff += 1
            
        if same == diff:
            result += 1
            same, diff = 0, 0
            temp = ''
    
    if dq:
        result += 1
    return result