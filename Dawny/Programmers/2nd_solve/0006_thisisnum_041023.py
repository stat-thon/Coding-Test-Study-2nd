# 1st
def solution(n):
    
    # 기본값
    cnt = 0
    
    # 1부터 n까지 작동
    for i in range(1,n+1):
        hap = 0
        p = i
        
        # n을 넘지 않을때 까지 합을 구함
        while hap < n:
            hap += p
            p += 1
            
        # hap이 n이랑 같으면 카운트
        if hap == n:
            cnt += 1 
            
    return cnt
  
# 2nd
from collections import deque
def solution(n):
    q = deque([j+1 for j in range(n)])
    stack = deque()
    hap = 0
    cnt = 0
    while q:
        if hap < n:
            stack.append(q.popleft())
            hap += stack[-1]
        elif hap == n:
            cnt += 1
            hap -= stack.popleft()
        else:
            hap -= stack.popleft()
    
    while stack:
        if hap == n:
            cnt += 1
        hap -= stack.popleft()
        
    return cnt
# 이중 반복보다 q를 활용한 코드가 속도가 더 빠른것을 확인할 수 있었음.
