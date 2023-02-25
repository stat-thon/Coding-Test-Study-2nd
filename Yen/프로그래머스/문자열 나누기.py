def solution(s):
    answer = 0
    if len(s)==1:
        return 1
    while s :
        a=1
        b=0
        for i in range(1,len(s)):
            if s[0]==s[i]:
                a +=1
            else: b +=1
            if a==b :
                break 
        answer +=1
        s= s[i+1:]
    return answer
