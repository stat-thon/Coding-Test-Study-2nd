def solution(s):    
    result = [-1] * len(s)
    
    for i in range(1, len(s)):
        if s[i] in s[:i]:
            result[i] = len(s[:i]) - s[:i].rfind(s[i])
        
    return result