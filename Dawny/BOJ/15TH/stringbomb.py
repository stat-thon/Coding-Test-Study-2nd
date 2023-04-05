# module
import sys

# input
input = sys.stdin.readline
s = input().rstrip()
bomb = input().rstrip()
stack = []
n = len(bomb)

for i in s:
    stack.append(i)
    if ''.join(stack[-n:]) == bomb:
        for _ in range(n):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print('FRULA')
