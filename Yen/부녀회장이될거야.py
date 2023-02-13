n = int(input())

for _ in range(n):  
    f = int(input())  
    b = int(input())  
    a = [x for x in range(1, b+1)]
    for k in range(f):  
        for i in range(1, b):  
            a[i] += a[i-1]  
    print(a[-1])
