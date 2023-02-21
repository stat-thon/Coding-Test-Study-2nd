def solution(d, budget):
    result = 0
    for num in sorted(d):
        budget -= num
        if budget < 0:
            break
        result += 1
    
    return result