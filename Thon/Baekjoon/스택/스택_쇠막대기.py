from collections import deque
dq = deque(input())
stack = []
cnt = 0

while dq:
    
    p = dq.popleft()
    
    if p == '(' and dq[0] == ')':
        dq.popleft()
        cnt += len(stack)
    
    elif p == '(' and dq[0] != ')':
        stack.append(p)
    
    elif p == ')':
        stack.pop()
        cnt += 1

print(cnt)
        