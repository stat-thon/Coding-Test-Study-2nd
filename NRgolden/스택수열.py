from collections import deque
n = int(input())


arr = deque([i for i in range(1,n+1)])
stack=[]
answer=[]
answer2 = []
cnt =1

for _ in range(n):
    
    num = int(input())
    
    while num>=cnt:
        stack.append(arr.popleft())
        answer2.append('+')
        cnt+=1
        
    if stack[-1]==num:
        answer.append(stack.pop())
        answer2.append('-')

if len(stack)!=0:
    print('NO')
else:
    for i in answer2:
        print(i)
