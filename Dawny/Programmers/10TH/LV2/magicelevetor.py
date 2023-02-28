def solution(storey):
    cnt = 0
    while storey:
        p, q = divmod(storey, 10)
        cnt += min(q, 10-q)
        if q > 5 :
            p += 1
        elif q == 5 and p % 10 >= 5:
            p += 1
        storey = p
    return cnt
