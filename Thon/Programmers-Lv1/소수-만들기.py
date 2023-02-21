def is_prime(n):
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

from itertools import combinations

def solution(nums):
    
    result = 0
    for a, b, c in combinations(nums, 3):
        if is_prime(a + b + c):
            result += 1
    return result