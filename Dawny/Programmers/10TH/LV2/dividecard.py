def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]
    for i in arrayA[1:]:
        a = gcd(a, i)
    for j in arrayB[1:]:
        b = gcd(b, j)
        
    if any(k % b == 0 for k in arrayA):
        b = 0
    if any(k % a == 0 for k in arrayB):
        a = 0
        
    return max(a, b)
    
