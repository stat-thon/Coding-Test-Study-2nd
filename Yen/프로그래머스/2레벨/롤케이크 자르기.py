def solution(topping):
    answer = 0
    topping_d=dict()
    a_d=dict()
    for i in topping :
        if i not in topping_d :
            topping_d[i] =1
        else: topping_d[i] +=1
    
    while len(topping) >=1 :
        x=topping.pop()
        if x not in a_d:
            a_d[x]=1 
            topping_d[x] -=1
        else: 
            a_d[x] +=1
            topping_d[x] -=1
        if topping_d[x]==0 :
            del topping_d[x]
        

        if len(topping_d.keys())==len(a_d.keys()):
            answer +=1

    return answer
