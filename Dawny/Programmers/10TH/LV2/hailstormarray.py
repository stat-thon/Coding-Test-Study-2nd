def lotharcollartz(k):
    l = [k]
    while k > 1:
        if k % 2 == 1:
            k = k*3 + 1
        else:
            k //= 2
        l.append(k)
    
    return l

def solution(k, ranges):
    y = lotharcollartz(k)
    s = [(a+b)/2 for a, b in zip(y[:-1], y[1:])]
    r = []
    for i in ranges:
        if i[0] > (len(y)+i[1]-1):
            r.append(-1.0)
        elif i[0] == (len(y)-1+i[1]):
            r.append(0.0)
        else:
            r.append(sum(s[i[0]:(len(y)+i[1]-1)]))
    return r
