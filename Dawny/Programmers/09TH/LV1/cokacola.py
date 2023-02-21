def solution(a, b, n):
    cnt = 0
    while n >= a:
        p, q = divmod(n, a)
        cnt += p*b
        n = p*b + q
        
    return cnt
