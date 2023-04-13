import re
while True:
    s = input()
    stack=[]
    if s=='.':
        break
        
    s= ''.join(re.findall('[\[\]\(\)]',s))
    
    for i in s:
        
        if i=='(' or i==')':
            if stack and (stack[-1]=='(' and i==')'):
                stack.pop()
            else:
                stack.append(i)
        if i=='[' or i==']':
            
            if stack and (stack[-1]=='[' and i==']'):
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        print('yes')
    else:
        print('no')
