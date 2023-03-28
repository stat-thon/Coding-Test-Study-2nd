def solution(n, s):
    if n > s:
        return [-1]
    p, q = divmod(s, n)
    l = [p]*n
    if q != 0:
        for i in range(n-1, n-q-1, -1):
            l[i] += 1
            
    return l
