n=int(input())
arr=list(map(int,input().split()))

stack=[]
result=[-1 for _ in range(n)]
for i,j in enumerate(arr):
    while stack and stack[-1][1] < j:
        result[stack[-1][0]]=j
        stack.pop()
    stack.append((i,j))

print(*result)
