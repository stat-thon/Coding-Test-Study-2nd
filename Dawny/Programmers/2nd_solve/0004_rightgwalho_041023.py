# 1st
def solution(s):
    
    if s.count('(') != s.count(')'):
        return False
    
    opened = 0
    closed = 0
    for i in s:
        if i == '(':
            opened += 1
        else:
            closed += 1
        
        if opened < closed:
            return False
        
    return True
    
# 2nd
def solution(s):
    cnt = 0
    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False
# 저번이랑 풀이 
