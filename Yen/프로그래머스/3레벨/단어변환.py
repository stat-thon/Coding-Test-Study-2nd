from collections import deque
def solution(begin, target, words):
    if target not in words :
        return 0
    
    q=deque([(begin,0)])
    while q :
        visited=[0]*len(words)
        x,c=q.popleft()
        if x==target :
            break
        for i in range(len(words)) :
            for j in range(len(words[i])) :
                if x[j]==words[i][j]:
                    visited[i] +=1
        for k in range(len(visited)):
            if visited[k]==(len(target)-1):
                q.append((words[k],c+1))
                words[k] = str(c)
                
    return c
