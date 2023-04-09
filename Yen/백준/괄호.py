n=int(input())
arr=[]
for i in range(n) :
    arr.append(input())
    
for i in arr :
    stack=[]
    for j in i :
        if stack==[] or j=='(':
            stack.append(j)
        elif stack[-1]=='(' and j==')':
            stack.pop()
    if stack== [] :
        print('YES')
    else:
        print('NO')
