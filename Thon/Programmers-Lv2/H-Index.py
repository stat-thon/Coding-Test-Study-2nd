def solution(citations):
    
    n = len(citations)
    
    while n >= 0:
        
        cnt = 0
        
        for cite in citations:
            if cite >= n:
                cnt += 1
        
        if n <= cnt :
            return n
        
        n -= 1