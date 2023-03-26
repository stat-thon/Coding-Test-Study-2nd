def solution(k, d):
    x = 0
    cnt = 0
    while x <= d:
        y = (d**2 - x**2)**0.5
        cnt += y//k + 1
        x += k
    return cnt
