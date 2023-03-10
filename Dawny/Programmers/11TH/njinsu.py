def zinbub(num, n):
    rest = "0123456789ABCDEF"
    k = ''
    while num >= n:
        x, y = divmod(num, n)
        num = x
        k = rest[y] + k
    return rest[num] + k


def solution(n, t, m, p):
    end = (t-1) * m + p
    y = ''
    c = 0
    while len(y) < end:
        y += zinbub(c, n)
        c += 1

    r = ''
    for i in range(p-1, end, m):
        r += y[i]
    return r
