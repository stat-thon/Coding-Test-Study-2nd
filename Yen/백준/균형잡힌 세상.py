a=[]
while True:
    i=input()
    if i=='.':
        break
    else: 
        a.append(i)
for i in a :
    stack=[]
    
    for j in i:
        
        if stack==[] and (j==')' or j==']'):
            stack.append(j)
            break
            
        if j=='(' or j=='[':
            stack.append(j)
        elif j ==')' :
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                break
        elif j==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else: break
        
    if stack==[]:
        print('yes')
    else: print('no')
