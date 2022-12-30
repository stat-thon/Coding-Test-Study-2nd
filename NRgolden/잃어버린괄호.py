def find_min(eq):
    
    eq_lst = eq.split('-')
    for i,n in enumerate(eq_lst):
        if i==0:
            try:
                answer=int(n)
            except:
                answer =sum(list(map(int,n.split('+'))))
            continue
        if n.isalnum()==True:
            answer-=int(n)
        else:
            answer-=sum(list(map(int,n.split('+'))))

    return answer

eq = input()
answer = find_min(eq)

print(answer)
