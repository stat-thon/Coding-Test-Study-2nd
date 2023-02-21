def solution(a, b, n):
    result = 0
    additional_coke = 0
    
    while n >= a:
        n, nam = divmod(n, a)
        n *= b
        result += n
        additional_coke += nam
            
        if n // a != (n + additional_coke) // a:
            n += additional_coke
            additional_coke = 0
            
    return result