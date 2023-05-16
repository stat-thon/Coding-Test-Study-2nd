from collections import deque

dq = deque([s for s in input()])
stack = []

while dq:
    
    stack.append(dq.popleft())
    if len(stack) >= 4:
        if ''.join(stack[-4:]) == 'PPAP':
            for _ in range(4):
                stack.pop()
            stack.append('P')
            
if stack == ['P']:
    print('PPAP')
else:
    print('NP')
