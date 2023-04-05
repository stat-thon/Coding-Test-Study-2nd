# module
import sys

# input
input = sys.stdin.readline

string = input().rstrip()
stack = []
reversestring = []

for i in string+" ":
    if i != " ":
        stack.append(i)
    else:
        while stack:
            reversestring.append(stack.pop())
        reversestring.append(' ')

print(''.join(reversestring[:-1]))
