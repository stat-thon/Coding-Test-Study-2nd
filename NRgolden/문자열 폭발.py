import sys
s = sys.stdin.readline().rstrip()
w = sys.stdin.readline().rstrip()
s_lst = list(s)
stack=[]
w_len =len(w)
w_last= w[-1]
for i in s_lst:
    stack.append(i)
    if stack[-1]==w_last and ''.join(stack[-w_len:])==w:
        for _ in range(w_len):
            stack.pop()

if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))
