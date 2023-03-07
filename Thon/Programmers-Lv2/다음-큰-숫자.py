def solution(n):
    num_one = len([i for i in bin(n)[2:] if int(i) == 1])
    
    a = n << 1
    n += 1
    while n < a:
        if num_one == len([i for i in bin(n)[2:] if int(i) == 1]):
            return n
        n += 1