def solution(today, terms, privacies):
    t = list(map(lambda x: list(x.split(' ')), terms))
    dic = {a:int(b) for a, b in t}
    ty, tm, td = map(int, today.split('.'))
    fake = []
    for j, i in enumerate(privacies):
        cy, cm, cd, g = i.replace('.',' ').split(' ')
        date = ((ty - int(cy))*12 + (tm - int(cm) - dic[g]))*28 + td - int(cd)
        if date >= 0:
            fake.append(j+1)
    return fake
