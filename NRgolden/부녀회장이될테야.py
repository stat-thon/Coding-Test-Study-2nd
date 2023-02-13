T = int(input())





def dfs(floor,room):
    
    if dy[floor][room]>0:
        return dy[floor][room]
    
    
    if floor==0:
        for i in range(1,room+1):
            dy[floor][i] = i
        return dy[floor][i]
    
    
    else:
        for i in range(1,room+1):
            dy[floor][room] +=  dfs(floor-1,i)
            
        return dy[floor][room]


for i in range(T):
    k = int(input())   
    n = int(input())
    dy = [[0]*(n+1) for _ in range(k+1)]
    
    dfs(k,n)
    
    print(dy[k][n])

