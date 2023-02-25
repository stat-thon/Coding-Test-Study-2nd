def solution(today, terms, privacies):
    answer = []
    terms_dic = dict()
    today_year , today_month, today_day = map(int,today.split('.'))

    for j in terms:
        type, t = j.split(' ')
        terms_dic[type] = int(t)
        
        
    for k,i in enumerate(privacies):
        date, term = i.split(' ')
        new_year, month, new_day = map(int,date.split('.'))
        new_month = month + terms_dic[term]

        if new_month>12:
            while new_month>12:
                new_month-=12
                new_year+=1
                
                
        if today_year> new_year:
            answer.append(k+1)
        elif today_year< new_year:
            continue
        else:
            if today_month>new_month:
                answer.append(k+1)
            elif today_month<new_month:
                continue
            else:
                if today_day>= new_day:
                    answer.append(k+1)      

            
    return answer
