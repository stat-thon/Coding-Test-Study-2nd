def solution(today, terms, privacies):
    result = []
    today = [int(i) for i in today.split('.')]
    now = (today[0] - 2000) * 12 * 28 + (today[1] - 1) * 28 + (today[2] - 1)
    term_dict = {t.split()[0]:int(t.split()[1]) for t in terms}
    
    for num, person in enumerate(privacies):
        date, term = person.split()
        agree_date = [int(i) for i in date.split('.')]
        dday = (agree_date[0] - 2000) * 12 * 28 + (agree_date[1] - 1) * 28 + (agree_date[2] - 1)
        dday += term_dict[term] * 28 - 1
        
        if now > dday:
            result.append(num + 1)
            
    return result