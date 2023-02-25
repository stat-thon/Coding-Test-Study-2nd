def Day(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    answer = []
    
    today = Day(today)
    
    t = dict()
    for term in terms:
        term = term.split()
        t[term[0]] = int(term[1]) * 28
    
    
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if Day(date) + t[term] <= today:
            answer.append(i+1)
        
    return answer
