def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]     
    for i in babbling:                 
        for v in speak:                 
            if v*2 not in i:           
                i=i.replace(v,' ')      
        if i.strip()=='':              
            answer+=1                   
    return answer
