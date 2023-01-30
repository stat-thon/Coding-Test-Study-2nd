d = [(0,1),(1,0),(1,2),(2,1),(2,0),(0,2)]
result=set()
result.add(w[2])
visited=[]
visited.append([0,0,w[2]])
def dfs(a,b,c):
    
    water_lst = [a,b,c]
#     print(water_lst)
    
    for i in range(6):
        now_water =[ water_lst[0], water_lst[1] , water_lst[2]]
        nd =d[i]
        now_w , next_w = nd
        
        if water_lst[now_w]!=0:
            mw = min(w[next_w] - now_water[next_w], now_water[now_w] )
            now_water[now_w]  = now_water[now_w] - mw
            now_water[next_w] = now_water[next_w] + mw
            if now_water in visited:
                continue
                
            else:
                visited.append(now_water)
                
                if now_water[0]==0:
                    result.add(now_water[2])

                dfs(now_water[0],now_water[1],now_water[2])
            
dfs(0,0,w[2])
print(*sorted(list(result)))
