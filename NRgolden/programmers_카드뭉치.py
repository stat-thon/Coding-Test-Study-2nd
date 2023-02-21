def solution(cards1, cards2, goal):
    answer = ''
    g_L = len(goal)
    c1_L = len(cards1)
    c2_L = len(cards2)
    c1_p = 0
    c2_p = 0
    w_lst = []
    for i in range(g_L):
        w = goal[i]
        if c1_p <c1_L and w==cards1[0]:
            cards1.pop(0)
            c1_p+=1
        elif c2_p <c2_L and  w==cards2[0]:
            cards2.pop(0)
            c2_p+=1
        else:
            return "No"
            
            
            
        
        
    return "Yes"
