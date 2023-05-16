import sys
n = input()
s = sys.stdin.readline()
num_lst =list(map(int,s.rstrip().split()))


stack=[]
answer=[-1]*len(num_lst)
for i in range(len(num_lst)):
    while stack and num_lst[stack[-1]]< num_lst[i]:
        q = stack.pop()
        answer[q]=num_lst[i]

    stack.append(i)

print(*answer)
