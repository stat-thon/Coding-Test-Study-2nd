# input
n, *c = map(int, open(0).read().split())
stack = []
visit = [0] * n
for i in range(n):
    while stack and c[stack[-1]] < c[i]:
        stack.pop()
    if stack:
        visit[i] = stack[-1] + 1
    stack.append(i)

print(*visit)
