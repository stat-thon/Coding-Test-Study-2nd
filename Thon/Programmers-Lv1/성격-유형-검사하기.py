def solution(survey, choices):
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
             'J': 0, 'M': 0, 'A':0, 'N': 0}
    
    for q, a in zip(survey, choices):
        if a > 4:
            score[q[1]] += a - 4
        elif a < 4:
            score[q[0]] += 4 - a
    
    result = ''
    for a, b in zip('RCJA', 'TFMN'):
        if score[a] >= score[b]:
            result += a
        else:
            result += b
            
    return result