def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

def solution(n, k):
    answer = []
    num=[]
    for i in range(1,n+1):
        num.append(i)
        
    x= (k-1) // factorial(n-1)
    answer.append(num[x])
    num.remove(num[x])
    
    while num :
        k= k % factorial(n-1)
        n -=1
        
        x= (k-1) // factorial(n-1)
        answer.append(num[x])
        num.remove(num[x])
        
    return answer
