# 못 풀겠어서 답 봄
# 괄호를 닫으면서 나누는 연산

parent = input()
stack, answer, tmp = [], 0, 1

for i in range(len(parent)):
    
    char = parent[i]

    if char == "(":
        stack.append(char)
        tmp *= 2

    elif char == "[":
        stack.append(char)
        tmp *= 3

    elif char == ")":
        
        if not stack or stack[-1] == "[":
            answer = 0
            break
            
        if parent[i - 1] == "(":
            answer += tmp
        
        stack.pop()
        tmp //= 2

    else:
        
        if not stack or stack[-1] == "(":
            answer = 0
            break
            
        if parent[i - 1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack: print(0)
else: print(answer)