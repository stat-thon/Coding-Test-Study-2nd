def solution(number, limit, power):
    result = 0
    sqrt_set = {i for i in range(1, 317)}
    for num in range(1, number + 1):
        n = 0
        
        for j in range(1, int(num ** 0.5) + 1):
            if num % j == 0:
                n += 1
        
        if num ** 0.5 in sqrt_set:
            n = 2 * (n - 1) + 1
        else:
            n *= 2
        
        if n > limit:
            result += power
        else:
            result += n
            
    return result