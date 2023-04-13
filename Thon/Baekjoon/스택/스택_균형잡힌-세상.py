while True:
    words = input()
    stack = []
    
    if words == '.':
        break
    
    for i in words:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
                
        elif i == ')':
            
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('no')
    else:
        print('yes')


# 다시 내 풀이
def is_parent(word):

    pdict = {')': '(', ']': '['}
    stack = []

    for char in word:
        if char not in pdict:
            stack.append(char)

        elif not stack or pdict[char] != stack.pop():
            return 'no'
    
    if len(stack) == 0:
        return 'yes'
    
    return 'no'

while True:
    
    i = input()
    
    if i == '.':
        break
        
    one = []
    for s in i:
        if s == '.':
            print(is_parent(one))

        elif s in ('(', ')', '[',']'):
            one.append(s)
