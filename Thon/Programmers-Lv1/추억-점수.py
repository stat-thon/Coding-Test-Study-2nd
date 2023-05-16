def solution(name, yearning, photo):
    ydict = {n:y for n, y in zip(name, yearning)}
    
    answer = []
    for p in photo:
        score = 0
        for people in p:
            if people in ydict:
                score += ydict[people]
        answer.append(score)
    return answer