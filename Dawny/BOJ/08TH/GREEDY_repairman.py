# module
from collections import deque

# input
n, l = map(int, input().split())

# greedy
hole = deque(sorted(list(map(int, input().split()))))

cnt = 0
store = 0
length = 1
while hole:
    a = hole.popleft()
    b = a - store
    if store == 0:
        store += a
    elif l - length >= b:
        store += b
        length += b
    else:
        cnt += 1
        store = a
        length = 1
print(cnt+1)
