# module
from collections import deque
import sys

# input
input = sys.stdin.readline
left = deque(input().rstrip())
n = int(input())
right = deque([])

for _ in range(n):
    module = input().rstrip()
    if module[0] == 'P':
        a, b = module.split(" ")
        left.append(b)

    elif module == 'L':
        if left:
            right.appendleft(left.pop())

    elif module == 'D':
        if right:
            left.append(right.popleft())

    else:
        if left:
            left.pop()

print(''.join(left) + ''.join(right))
