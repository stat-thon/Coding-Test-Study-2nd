from collections import deque 

def solution(n, m, section):
    answer = 0
    q=deque(section)
    while q :
        x=q.popleft()
        while q and q[0] < x+m :
            q.popleft()
        answer +=1
    
    return answer
