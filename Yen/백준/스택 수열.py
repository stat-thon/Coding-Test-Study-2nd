n=int(input())
arr=[int(input()) for _ in range(n)]
num= [ i+1 for i in range(n)]

stack=[]
p=[]

for i in arr:
    if stack==[]:
        stack.append(num.pop(0))
        p.append('+')
    
    while stack :
        
        if stack[-1]> i :
            break
        
        if stack[-1]==i :
            p.append('-')
            stack.pop()
            break
            
        if stack[-1]<i and num :
            p.append('+')
            stack.append(num.pop(0))
            
    
    
if stack==[]:
    for i in p:
        print(i)
else:
    print('NO')
