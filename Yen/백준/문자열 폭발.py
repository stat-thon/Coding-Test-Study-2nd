import sys

r=sys.stdin.readline().rstrip()
boom=sys.stdin.readline().rstrip()

stack=[]
for i in range(len(r)):
    stack.append(r[i])
    while ''.join(stack[-len(boom):])==boom:
        for _ in range(len(boom)):
            stack.pop()

if stack==[]:
    print('FRULA')
else: print(''.join(stack))
