# 1st
def solution(n):
    
    a = [0,1]
    for i in range(2,n+1):
        a += [a[i-1]+a[i-2]]
    return a[-1] % 1234567
  
# 2nd
def solution(n):
    l = [0, 1]
    for _ in range(n):
        l = [l[1], sum(l)]
    
    return l[0] % 1234567
  
# 피보나치는 너무 심했다.
