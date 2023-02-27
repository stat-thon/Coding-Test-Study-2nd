def solution(s):
    answer = 0
    x_p=0
    no_x_p = 1
    x_cnt=1
    no_x_cnt = 0
    while True:
        if len(s)==1:
            answer+=1
            break
        
        x = s[x_p]
        no_x = s[no_x_p]
        if x != no_x:
            if len(s)==2:
                answer+=1
                break
            no_x_cnt+=1
        else:
            x_cnt+=1
        if x_cnt==no_x_cnt:

            answer +=1
            s = s[no_x_p+1:]
            x_p = 0
            no_x_p=1
            x_cnt = 1
            no_x_cnt = 0
        else:
            no_x_p+=1
            if no_x_p==len(s)-1:
                answer+=1
                break   

            
            
        
    return answer
