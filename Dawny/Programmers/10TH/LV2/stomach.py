def solution(clothes):
    dic = {}
    for _, j in clothes:
        if j not in dic:
            dic.setdefault(j, 1)
        else:
            dic[j] += 1
    c = 1
    for k in dic.values():
        c *= (k+1)
    return c - 1
