def check(s):
    pdict = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for i in range(len(s)):
        
        if s[i] in pdict.keys() and stack:
            
            if s[stack[-1]] == pdict[s[i]]:
                stack.pop()
        
            else:
                return False
        
        else:
            stack.append(i)
        
    if stack:
        return False
        
    return True
        
def solution(s):
    cnt = 0
    for i in range(len(s)):
        cnt += check(s[i + 1:] + s[:i + 1])
    
    return cnt