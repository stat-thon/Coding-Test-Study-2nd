from collections import deque
word, explode = deque(input()), input()
stack = []
n = len(explode)

while word:
    stack.append(word.popleft())
    
    while ''.join(stack[-n:]) == explode:
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
    
    