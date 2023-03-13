from collections import deque
def solution(s):
    lst = list(s)
    answer=0
    for _ in range(len(s)):
        lst.append(lst.pop(0))
        stack =[]
        for i in range(len(lst)):
            if lst[i] in ['(',')']:
                if len(stack)>0 and (stack[-1]=='(' and  lst[i]==')'):
                    stack.pop()                
                else:
                    stack.append(lst[i])
            elif lst[i] in ['{','}']:
                if len(stack)>0 and (stack[-1]=='{' and  lst[i]=='}'):
                    stack.pop()                
                else:
                    stack.append(lst[i])
            elif lst[i] in ['[',']']:
                if len(stack)>0 and (stack[-1]=='[' and  lst[i]==']'):
                    stack.pop()                
                else:
                    stack.append(lst[i])
        if len(stack)==0:
            answer+=1
    return answer
