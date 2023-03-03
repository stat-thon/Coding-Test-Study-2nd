def solution(storey):
    
    stack = [0] + [int(n) for n in str(storey)]
    cnt = 0
    
    while stack:
        n = stack.pop()
        
        if n < 5 :
            cnt += n
        
        elif n == 5:
            if stack[-1] < 5:
                cnt += n
            else:
                cnt += 10 - n
                stack[-1] += 1
        
        else:
            cnt += 10 - n
            stack[-1] += 1
        
    return cnt