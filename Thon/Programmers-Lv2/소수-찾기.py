# define is_prime
def is_prime(n):
    
    if n in (0, 1):
        return False
        
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    
    return True


# result
def solution(numbers):
    
    from itertools import permutations    
    
    result = set()
    
    for i in range(1, len(numbers) + 1):
        for t in permutations(numbers, i):
            new = int(''.join(t))
            
            if is_prime(new):
                result.add(new)
        
    return len(result)