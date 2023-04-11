from collections import deque
dq = deque(input())
stack = []
result = []

while dq:
    q = dq.popleft()
    
    if q == '<':
        result += stack[::-1]
        stack = []
        stack.append(q)
        
        while True:
            nq = dq.popleft()
            stack.append(nq)
            if nq == '>':
                result += stack
                stack = []
                break
                
    elif q == ' ':
        result += stack[::-1]
        result.append(' ')
        stack = []
        
    else:
        stack.append(q)

result += stack[::-1]

print(''.join(result))