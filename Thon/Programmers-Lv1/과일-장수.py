def solution(k, m, score):
    stack = sorted(score)
    result = 0
    while len(stack) >= m:
        for _ in range(m):
            s = stack.pop()
        
        result += s * m
    
    return result