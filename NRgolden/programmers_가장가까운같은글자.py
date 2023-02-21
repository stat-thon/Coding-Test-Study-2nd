def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] in dic:
            answer.append(i - dic[s[i]])
                
        else:
            answer.append(-1)
        dic[s[i]] = i
    return answer
