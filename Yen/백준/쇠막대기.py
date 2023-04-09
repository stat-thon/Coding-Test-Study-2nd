import sys

p=sys.stdin.readline().strip()

stack=[]
c=0

for i in range(len(p)):
    if p[i]=='(':
        stack.append('(')
    elif p[i]==')' and p[i-1]=='(':
        stack.pop()
        c+= len(stack)
    elif p[i]==')' and p[i-1]==')' :
        stack.pop()
        c +=1
print(c)
