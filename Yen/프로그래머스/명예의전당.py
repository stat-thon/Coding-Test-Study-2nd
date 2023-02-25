def solution(k, score):
    answer = []
    r=[]
    while score :
        r.append(score[0])
        score.remove(score[0])
        if len(r) >k:
            a=min(r)
            if a<r[-1]:
                r.remove(a)
            else:
                r.remove(r[-1])
        answer.append(min(r))
    return answer
