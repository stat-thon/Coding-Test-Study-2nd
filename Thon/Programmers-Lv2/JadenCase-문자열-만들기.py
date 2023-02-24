def solution(s):
    
    jaden = ''
    temp = ' '
    for i in range(len(s)):
        
        if temp == ' ':
            if s[i].isalpha():
                jaden += s[i].upper()
            else:
                jaden += s[i]
            temp = s[i]
        
        else:
            if s[i] != ' ':
                jaden += s[i].lower()
                temp = s[i]
            
            else:
                jaden += s[i]
                temp = s[i]
    
    return jaden