from collections import deque

def solution(s):
    a1, a2, a3 = s.count('{'), s.count('('), s.count('[')
    b1, b2, b3 = s.count('}'), s.count(')'), s.count(']')
    if a1 - b1 != 0 or a2 - b2 != 0 or a3 - b3 != 0:
        return 0
    
    stack = ['0']
    cnt = 0
    h = 0
    q = deque(s)
    while cnt < len(s):
        cnt += 1
        r = q.copy()
        while r:
            a = r.popleft()
            if a in ["{", "(", "["]:
                stack.append(a)
            elif a == "}" and stack[-1] == "{":
                stack.pop()
            elif a == ")" and stack[-1] == "(":
                stack.pop()
            elif a == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack = ['0']
                break
                
        if stack[-1] == '0' and len(r) == 0:
            h += 1

        q.append(q.popleft())
    
    return h
