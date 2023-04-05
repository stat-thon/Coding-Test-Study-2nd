# module
import sys

# input
input = sys.stdin.readline

string = input().rstrip()
stack = []
rs = []
k = 0

for i in string+" ":
    if k == 1 and i != ">":
        rs.append(i)
        continue

    elif k == 1 and i == ">":
        rs.append(i)
        k = 0
        continue

    if i == "<":
        k = 1
        while stack:
            rs.append(stack.pop())
        rs.append(i)
    elif i != ' ':
        stack.append(i)
    else:
        while stack:
            rs.append(stack.pop())
        rs.append(' ')

print(''.join(rs[:-1]))
