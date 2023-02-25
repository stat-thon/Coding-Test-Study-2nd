def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1,len(s)):
        for j in range(i-1,-1,-1):
            c=0
            if s[i]==s[j]:
                c=i-j
                answer.append(c)
                break
        if c==0:
            answer.append(-1)
    return answer
