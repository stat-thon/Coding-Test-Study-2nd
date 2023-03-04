import heapq
from collections import deque

def solution(n, k, enemy):
    answer=0
    s=[]
    q=deque(enemy)
    
    while q :
        i=q.popleft()
        
        if n >= i :
            n -= i
            heapq.heappush(s,-i)
            answer +=1
        elif n< i and k >=1 :
            if s==[] :
                k -=1
            elif s and i > -s[0]:
                k -= 1
            else:
                n -= i
                k -=1
                a=heapq.heappop(s)
                heapq.heappush(s,-i)
                n -= a
            answer +=1
        else:
            break
    return answer
