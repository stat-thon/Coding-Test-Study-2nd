def treenum(b):
    l = len(b)
    x, y = 1, 2
    cnt = 0
    while not x <= l < y:
        x *= 2
        y *= 2
        cnt += 1
        
    return "0"*(y-l-1) + b, cnt

def solution(numbers):
    
    def dfs(n, p, num):
        if p == 0 and t[n] == "1":
            return 0
        
        if num == 0:
            return 1
        
        else:
            k1 = dfs(n - (2**(num - 1)), int(t[n]), num - 1)
            k2 = dfs(n + (2**(num - 1)), int(t[n]), num - 1)
            if k1 + k2 < 2:
                return 0
            
            else:
                return 1
    
    dab = []
    for i in numbers:
        b = bin(i)[2:]
        t, deep = treenum(b)
        dab.append(dfs(int((len(t)-1)/2), 1, deep))
    
    return dab
