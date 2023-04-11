from collections import deque
dq, stack, result = deque(input()), deque(), deque()

while dq:
    q = dq.popleft()
    
    if q == '<':
        result += stack
        stack = deque(q)
        
        while True:
            nq = dq.popleft()
            stack.append(nq)
            
            if nq == '>':
                result += stack
                stack = deque()
                break
                
    elif q == ' ':
        result += stack
        result.append(' ')
        stack = deque()
        
    else:
        stack.appendleft(q)
        
result += stack
print(''.join(result))