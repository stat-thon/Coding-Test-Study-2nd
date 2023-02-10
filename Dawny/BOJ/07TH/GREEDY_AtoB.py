# module
from collections import deque
# input
a, b = map(int, input().split())


# bfs
def bfs(first, end):
    q = deque([[first, 1]])
    while q:
        node, cnt = q.popleft()
        if node == end:
            return cnt
        i = node*2
        ii = node*10 + 1
        if i <= end:
            q.append([i, cnt+1])
        if ii <= end:
            q.append([ii, cnt+1])
    return -1


if a*2 > b:
    print(-1)
else:
    print(bfs(a, b))
