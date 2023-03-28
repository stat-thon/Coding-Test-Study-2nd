from collections import deque
def solution(begin, target, words):
    n = len(words)
    nword = len(begin)
    q = deque([[begin, 0]])
    while q:
        
        a, b = q.popleft()
        if a == target:
            return b
        
        for i in range(n):
            cnt = 0
            for j in range(nword):
                if a[j] == words[i][j]:
                    cnt += 1
                    
            if cnt == nword - 1:
                q.append([words[i], b+1])
                words[i] = "0" * nword
                
    return 0
