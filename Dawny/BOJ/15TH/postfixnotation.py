# module
import sys

# input
input = sys.stdin.readline
s = input().rstrip()
sick = []
stack = []
dic = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
for i in s:
    if i.isalpha():
        sick.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            sick.append(stack.pop())
        stack.pop()
    else:
        while stack and dic[i] <= dic[stack[-1]]:
            sick.append(stack.pop())
        stack.append(i)

while stack:
    sick.append(stack.pop())
print(''.join(sick))
