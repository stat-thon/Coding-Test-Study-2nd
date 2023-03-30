def fivejinsu(num):
    p, q = divmod(num, 5)
    return fivejinsu(p) + str(q) if p != 0 else str(q)

def kantor(s):
    cnt = 0
    le = len(s)
    label = [0, 1, 2, 2, 3]
    for i in s:
        le -= 1
        cnt += (4**le)*label[int(i)]
        if int(i) == 2 :
            break
    return cnt

def solution(n, l, r):

    return kantor(fivejinsu(r)) - kantor(fivejinsu(l - 1))
