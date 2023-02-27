def solution(number):
    answer=0
    def dfs(L,S,list):
        nonlocal answer
        if L==3:
            if sum(list)==0:
                answer+=1
                return
        
        else:
            for i in range(S,len(number)):
                dfs(L+1,i+1,list+[number[i]])
    dfs(0,0,[])            
    return answer
