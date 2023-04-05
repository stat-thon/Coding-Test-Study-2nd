from collections import deque

while True:
    stack = deque([])
    n = input()
    if n == ".":
        break

    q = deque(n)
    while q:
        a = q.popleft()
        if a in ['(', '[']:
            stack.append(a)
        elif a == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('안만들어짐!')
                break
        elif a == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('안만들어짐!')
                break

    if stack:
        print("no")
    else:
        print("yes")
