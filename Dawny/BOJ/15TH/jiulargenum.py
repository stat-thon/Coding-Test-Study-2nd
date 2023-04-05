# input
n, *c = map(int, open(0).read().split())

visit = [-1] * n
stack = []
for i in range(n):
    while len(stack) != 0 and c[stack[-1]] < c[i]:
        visit[stack[-1]] = c[i]
        stack.pop()
    stack.append(i)
print(*visit)
