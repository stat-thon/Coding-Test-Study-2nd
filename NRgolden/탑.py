import sys
n = int(input())
s = sys.stdin.readline()
top = list(map(int,s.rstrip().split()))

top_r = top[::-1]
stack=[]
answer=[0]*len(top)
for i in range(n):
    while stack and top_r[stack[-1]] < top_r[i]:
        q = stack.pop()
        answer[len(top)-1-q]= len(top)-i

    stack.append(i)
    
print(*answer)
