from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])
stack = deque([])
sign = []
for _ in range(n):
    a = int(input())
    if stack and stack[-1] == a:
        stack.pop()
        sign.append("-")

    elif q and q[0] <= a:
        while q and q[0] < a:
            stack.append(q.popleft())
            sign.append('+')
        q.popleft()
        sign.append('+')
        sign.append('-')
    else:
        print("NO")
        break

else:
    for j in sign:
        print(j)
